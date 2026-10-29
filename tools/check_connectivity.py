"""Gửi MỘT request an toàn (GET) tới mỗi API để kiểm tra còn truy cập được hay không.

Chạy trên máy có Internet. API cần khóa sẽ đọc khóa từ biến môi trường ghi trong meta.yaml
(ví dụ OMDB_API_KEY). Kết quả ghi vào connectivity_report.json; thêm --update-meta để đánh dấu
environment.connectivity_checked = true cho các API trả về 2xx.

Dùng:  python tools/check_connectivity.py [--api ID] [--update-meta]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def probe(meta: dict) -> dict:
    env = meta["environment"]
    pr = env.get("probe") or {}
    if env.get("test_scope") == "none" or not pr.get("path") or pr.get("path") == "TODO":
        return {"status": "skipped", "reason": "không có probe hoặc test_scope = none"}
    params = dict(pr.get("params") or {})
    headers = {"User-Agent": "SpecLoop-Bench/0.1", "Accept": "application/json"}
    auth = env.get("auth") or {}
    if auth.get("type") not in (None, "none"):
        key = os.environ.get(auth.get("env_var") or "")
        if not key:
            return {"status": "skipped", "reason": f"thiếu biến môi trường {auth.get('env_var')}"}
        if auth["type"] == "apiKey" and auth.get("in", "query") == "query":
            params[auth.get("name", "apikey")] = key
        elif auth["type"] == "apiKey":
            headers[auth.get("name", "X-API-Key")] = key
        else:
            headers["Authorization"] = f"Bearer {key}"
    url = env["base_url"].rstrip("/") + "/" + pr["path"].lstrip("/")
    if params:
        url += "?" + urllib.parse.urlencode(params)
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers=headers, method=pr.get("method", "GET"))
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(300)
            return {"status": r.status, "latency_ms": round((time.time() - t0) * 1000), "url": url.split("?")[0],
                    "content_type": r.headers.get("content-type"), "sample": body.decode("utf-8", "replace")[:120]}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "latency_ms": round((time.time() - t0) * 1000), "url": url.split("?")[0]}
    except Exception as e:  # noqa: BLE001
        return {"status": "error", "error": str(e)[:200], "url": url.split("?")[0]}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--api")
    ap.add_argument("--update-meta", action="store_true")
    a = ap.parse_args()
    report = {"checked_at": dt.datetime.now().isoformat(timespec="seconds"), "results": {}}
    for d in sorted(x for x in (ROOT / "apis").iterdir() if x.is_dir() and not x.name.startswith("_")):
        if a.api and d.name != a.api:
            continue
        mp = d / "meta.yaml"
        meta = yaml.safe_load(mp.read_text(encoding="utf-8"))
        res = probe(meta)
        report["results"][d.name] = res
        ok = isinstance(res.get("status"), int) and 200 <= res["status"] < 300
        print(f"{'✓' if ok else '•'} {d.name:<20} {res.get('status')}  {res.get('latency_ms', '')} ms  {res.get('reason', res.get('error', ''))}")
        if ok and a.update_meta:
            text = mp.read_text(encoding="utf-8").replace("connectivity_checked: false", "connectivity_checked: true")
            mp.write_text(text, encoding="utf-8")
    (ROOT / "connectivity_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Đã ghi connectivity_report.json")


if __name__ == "__main__":
    main()
