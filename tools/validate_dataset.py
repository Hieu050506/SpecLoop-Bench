"""Kiểm tra tính toàn vẹn của bộ dữ liệu. Chạy sau mỗi lần thêm/sửa API.

Kiểm tra: meta.yaml đủ trường bắt buộc; tệp tồn tại; ground truth hợp lệ OAS 3.0.3;
facts.jsonl khớp với ground truth hiện tại; tài liệu đầu vào không rỗng; id fact không trùng;
discrepancies.json đúng cấu trúc; mã băm trong manifest.json khớp tệp.

Dùng:  python tools/validate_dataset.py [--api ID]
Mã thoát 0 = đạt, 1 = có lỗi.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_facts import extract, read_jsonl  # noqa: E402
from oas_utils import load_spec, sha256_file, validate_spec  # noqa: E402

REQUIRED_META = {
    "id": str, "name": str, "group": str, "description": str, "source": dict, "environment": dict,
    "docs": dict, "ground_truth": dict, "rq_scope": list,
}
ENV_FIELDS = ["type", "base_url", "test_scope", "auth"]
GROUPS = {"A", "B"}
ENV_TYPES = {"local-docker", "public", "offline"}
SCOPES = {"full", "read-only", "none"}
DISC_CODES = {f"D{i}" for i in range(10)}


def check_api(d: Path, manifest_files: dict) -> tuple[list, list]:
    errs, warns = [], []
    mp = d / "meta.yaml"
    if not mp.exists():
        return [f"thiếu meta.yaml"], warns
    meta = yaml.safe_load(mp.read_text(encoding="utf-8"))
    for k, t in REQUIRED_META.items():
        if k not in meta:
            errs.append(f"meta thiếu trường '{k}'")
        elif not isinstance(meta[k], t):
            errs.append(f"meta.{k} phải là {t.__name__}")
    if errs:
        return errs, warns
    if meta["id"] != d.name:
        errs.append(f"meta.id ({meta['id']}) khác tên thư mục ({d.name})")
    if meta["group"] not in GROUPS:
        errs.append(f"meta.group phải thuộc {GROUPS}")
    env = meta["environment"]
    for k in ENV_FIELDS:
        if k not in env:
            errs.append(f"meta.environment thiếu '{k}'")
    if env.get("type") not in ENV_TYPES:
        errs.append(f"environment.type phải thuộc {ENV_TYPES}")
    if env.get("test_scope") not in SCOPES:
        errs.append(f"environment.test_scope phải thuộc {SCOPES}")
    if "TODO" in mp.read_text(encoding="utf-8"):
        warns.append("meta.yaml còn chữ TODO cần điền")
    gt = d / "ground_truth" / "openapi.yaml"
    if not gt.exists():
        errs.append("thiếu ground_truth/openapi.yaml")
        return errs, warns
    spec = load_spec(gt)
    if spec.get("openapi") != "3.0.3":
        errs.append(f"ground truth phải là OpenAPI 3.0.3 (đang là {spec.get('openapi')})")
    errs += [f"ground truth không hợp lệ: {e}" for e in validate_spec(spec)]
    fpath = d / "ground_truth" / "facts.jsonl"
    if not fpath.exists():
        errs.append("thiếu facts.jsonl – chạy tools/build_dataset.py")
    else:
        saved = read_jsonl(fpath)
        ids = [f["id"] for f in saved]
        if len(ids) != len(set(ids)):
            errs.append("facts.jsonl có id trùng")
        fresh = {f["key"] for f in extract(spec)}
        if fresh != {f["key"] for f in saved}:
            errs.append("facts.jsonl không khớp ground truth hiện tại – chạy lại build_dataset.py")
    docs = meta["docs"]
    for k in ("original", "rendered", "ablated"):
        rel = docs.get(k)
        if rel:
            p = d / rel
            if not p.exists():
                errs.append(f"thiếu tài liệu {rel}")
            elif len(p.read_text(encoding="utf-8").split()) < 30:
                errs.append(f"tài liệu {rel} quá ngắn")
    if not docs.get("original"):
        warns.append("chưa có tài liệu gốc (docs/original.*) – mới chỉ có bản render từ OAS")
    beh = meta["ground_truth"].get("behavior")
    if beh:
        bp = d / beh
        if not bp.exists():
            errs.append(f"thiếu {beh}")
        else:
            errs += [f"behavior spec không hợp lệ: {e}" for e in validate_spec(load_spec(bp))]
    dp = d / "ground_truth" / "discrepancies.json"
    if dp.exists():
        data = json.loads(dp.read_text(encoding="utf-8"))
        for i, x in enumerate(data.get("discrepancies", [])):
            for k in ("id", "code", "op", "description", "doc", "behavior", "probe"):
                if k not in x:
                    errs.append(f"discrepancies[{i}] thiếu '{k}'")
            if x.get("code") not in DISC_CODES:
                errs.append(f"discrepancies[{i}].code không hợp lệ")
    for rel, h in manifest_files.items():
        p = ROOT / rel
        if not p.exists():
            errs.append(f"manifest liệt kê tệp không tồn tại: {rel}")
        elif sha256_file(p) != h:
            warns.append(f"tệp đã đổi so với manifest (chạy build_dataset.py): {rel}")
    if not env.get("connectivity_checked") and env.get("type") == "public":
        warns.append("chưa kiểm tra kết nối API công khai (tools/check_connectivity.py)")
    return errs, warns


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--api")
    a = ap.parse_args()
    man = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8")) if (ROOT / "manifest.json").exists() else {"apis": []}
    mfiles = {e["id"]: e.get("files", {}) for e in man["apis"]}
    total_err = 0
    for d in sorted(x for x in (ROOT / "apis").iterdir() if x.is_dir() and not x.name.startswith("_")):
        if a.api and d.name != a.api:
            continue
        if d.name not in mfiles:
            print(f"✗ {d.name}: chưa có trong manifest.json – chạy tools/build_dataset.py")
            total_err += 1
            continue
        errs, warns = check_api(d, mfiles.get(d.name, {}))
        mark = "✓" if not errs else "✗"
        print(f"{mark} {d.name}")
        for e in errs:
            print(f"    LỖI: {e}")
        for w in warns:
            print(f"    lưu ý: {w}")
        total_err += len(errs)
    print("\nKẾT QUẢ:", "ĐẠT" if total_err == 0 else f"{total_err} lỗi")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
