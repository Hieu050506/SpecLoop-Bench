"""Thêm một REST API mới vào bộ dữ liệu.

Ví dụ:
  python tools/add_api.py --id httpbin --name "httpbin" --group B \
      --spec https://raw.githubusercontent.com/<...>/openapi.yaml \
      --base-url https://httpbin.org --env public --scope read-only \
      --doc-original duong_dan/trang_tai_lieu.html --source-url https://httpbin.org \
      --license "ISC" --ablated

Script sẽ:
  1. tạo apis/<id>/ (source/, docs/, ground_truth/)
  2. lưu đặc tả gốc vào source/, chuẩn hóa về OpenAPI 3.0.3 -> ground_truth/openapi.yaml
  3. sao chép tài liệu gốc (nếu có) vào docs/original.<đuôi>
  4. sinh meta.yaml (các trường chưa biết ghi TODO), rồi chạy build + validate cho API đó
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
from oas_utils import dump_yaml, normalize_to_303, validate_spec  # noqa: E402


def fetch(src: str) -> tuple[bytes, str]:
    if re.match(r"^https?://", src):
        req = urllib.request.Request(src, headers={"User-Agent": "SpecLoop-Bench/0.1"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read(), Path(src.split("?")[0]).suffix or ".txt"
    p = Path(src)
    return p.read_bytes(), p.suffix or ".txt"


def parse_spec(raw: bytes, suffix: str) -> dict:
    text = raw.decode("utf-8")
    if suffix == ".json" or text.lstrip().startswith("{"):
        return json.loads(text)
    return yaml.safe_load(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--id", required=True, help="chữ thường, số, gạch nối; ví dụ my-api")
    ap.add_argument("--name", required=True)
    ap.add_argument("--group", choices=["A", "B"], required=True, help="A: tự triển khai/kiểm soát; B: công khai")
    ap.add_argument("--spec", required=True, help="đường dẫn hoặc URL tới OpenAPI 3.x (YAML/JSON)")
    ap.add_argument("--base-url", help="URL gốc dùng để kiểm thử (ghi đè servers[0].url)")
    ap.add_argument("--env", choices=["local-docker", "public", "offline"], default="public")
    ap.add_argument("--scope", choices=["full", "read-only", "none"], default="read-only")
    ap.add_argument("--auth", choices=["none", "apiKey", "bearer", "oauth2"], default="none")
    ap.add_argument("--auth-env", help="tên biến môi trường chứa khóa, ví dụ OMDB_API_KEY")
    ap.add_argument("--doc-original", help="tài liệu gốc viết cho con người (HTML/MD/PDF/TXT) – đường dẫn hoặc URL")
    ap.add_argument("--source-url", default="TODO")
    ap.add_argument("--docs-url", default="TODO")
    ap.add_argument("--license", default="TODO")
    ap.add_argument("--ablated", action="store_true", help="sinh thêm biến thể tài liệu lược ràng buộc")
    ap.add_argument("--force", action="store_true", help="ghi đè nếu thư mục đã tồn tại")
    a = ap.parse_args()

    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,40}", a.id):
        sys.exit("--id chỉ gồm chữ thường, số, gạch nối (2–41 ký tự)")
    d = ROOT / "apis" / a.id
    if d.exists() and not a.force:
        sys.exit(f"{d} đã tồn tại (dùng --force để ghi đè)")
    for sub in ("source", "docs", "ground_truth"):
        (d / sub).mkdir(parents=True, exist_ok=True)

    raw, suffix = fetch(a.spec)
    src_name = "openapi_original" + (suffix if suffix in (".json", ".yaml", ".yml") else ".yaml")
    (d / "source" / src_name).write_bytes(raw)
    spec = parse_spec(raw, suffix)
    try:
        spec, notes = normalize_to_303(spec)
    except ValueError as e:
        shutil.rmtree(d) if not a.force else None
        sys.exit(f"Không chuẩn hóa được: {e}")
    if a.base_url:
        old = (spec.get("servers") or [{}])[0].get("url")
        spec["servers"] = [{"url": a.base_url}]
        notes.append(f"servers[0].url: {old!r} -> {a.base_url!r}")
    errs = validate_spec(spec)
    if errs:
        print("CẢNH BÁO: đặc tả sau chuẩn hóa chưa hợp lệ – cần sửa tay ground_truth/openapi.yaml:")
        for e in errs:
            print("  -", e)
    dump_yaml(spec, d / "ground_truth" / "openapi.yaml")

    docs = {"original": None, "rendered": "docs/rendered.md", "ablated": "docs/ablated.md" if a.ablated else None,
            "make_ablated": bool(a.ablated)}
    if a.doc_original:
        draw, dsuf = fetch(a.doc_original)
        dsuf = dsuf if dsuf in (".md", ".html", ".htm", ".pdf", ".txt") else ".txt"
        (d / "docs" / f"original{dsuf}").write_bytes(draw)
        docs["original"] = f"docs/original{dsuf}"

    auth = {"type": a.auth}
    if a.auth != "none":
        auth["env_var"] = a.auth_env or "TODO"
    meta = {
        "id": a.id, "name": a.name, "group": a.group,
        "description": "TODO: mô tả ngắn API (lĩnh vực, số endpoint, điểm đáng chú ý về ràng buộc)",
        "source": {"spec_url": a.spec if a.spec.startswith("http") else "TODO", "spec_file": f"source/{src_name}",
                   "license": a.license, "homepage": a.source_url, "docs_url": a.docs_url,
                   "retrieved_at": dt.date.today().isoformat(), "normalization": notes},
        "environment": {"type": a.env, "base_url": a.base_url or (spec.get("servers") or [{}])[0].get("url", "TODO"),
                        "test_scope": a.scope, "auth": auth, "rate_limit_rps": 1 if a.env == "public" else 5,
                        "connectivity_checked": False,
                        "probe": {"method": "GET", "path": "TODO", "params": {}}},
        "docs": docs,
        "ground_truth": {"doc": "ground_truth/openapi.yaml", "behavior": None, "behavior_status": "pending",
                         "verified_by": [], "notes": "GT tài liệu = đặc tả chính thức; GT hành vi chưa xác minh."},
        "rq_scope": ["RQ1", "RQ2", "RQ3"] if a.scope != "none" else ["RQ1"],
        "added_by": "TODO", "notes": "",
    }
    (d / "meta.yaml").write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Đã tạo {d.relative_to(ROOT)}")
    for n in notes:
        print("  chuẩn hóa:", n)
    subprocess.run([sys.executable, str(TOOLS / "build_dataset.py"), "--api", a.id], check=True)
    subprocess.run([sys.executable, str(TOOLS / "validate_dataset.py"), "--api", a.id])
    print("\nViệc còn lại: mở meta.yaml điền các mục TODO (mô tả, giấy phép, probe kết nối), "
          "sau đó chạy lại: python tools/build_dataset.py --api", a.id)


if __name__ == "__main__":
    main()
