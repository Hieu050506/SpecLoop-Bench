"""Xem các API trong dataset: python tools/view_dataset.py (http://127.0.0.1:8765)."""
from __future__ import annotations

import argparse
from functools import lru_cache
from pathlib import Path

import yaml
from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, PlainTextResponse

ROOT = Path(__file__).resolve().parent.parent
API_ROOT = ROOT / "apis"
METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
app = FastAPI(title="SpecLoop · Dataset Explorer", docs_url=None, redoc_url=None, openapi_url=None)


def api_dir(api_id: str) -> Path:
    if not api_id or any(c not in "abcdefghijklmnopqrstuvwxyz0123456789-" for c in api_id):
        raise HTTPException(404, "Không tìm thấy API")
    directory = API_ROOT / api_id
    if not (directory / "meta.yaml").is_file():
        raise HTTPException(404, "Không tìm thấy API")
    return directory


def read_yaml(path: Path) -> dict:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))


@lru_cache(maxsize=32)
def spec_for(api_id: str) -> dict:
    return read_yaml(api_dir(api_id) / "ground_truth" / "openapi.yaml")


def info_for(api_id: str) -> dict:
    directory = api_dir(api_id)
    meta = read_yaml(directory / "meta.yaml")
    spec = spec_for(api_id)
    facts = directory / "ground_truth" / "facts.jsonl"
    with facts.open(encoding="utf-8") as source:
        fact_count = sum(bool(line.strip()) for line in source)
    return {
        "id": api_id,
        "name": meta["name"],
        "description": meta.get("description", ""),
        "group": meta["group"],
        "environment": meta["environment"]["type"],
        "base_url": meta["environment"].get("base_url", ""),
        "scope": meta["environment"]["test_scope"],
        "behavior_status": meta["ground_truth"].get("behavior_status", "pending"),
        "operations": sum(method in METHODS for item in spec.get("paths", {}).values()
                          if isinstance(item, dict) for method in item),
        "facts": fact_count,
        "docs": [kind for kind in ("original", "rendered", "ablated") if meta["docs"].get(kind)],
    }


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(Path(__file__).with_name("dataset_viewer.html"))


@app.get("/api/catalog")
def catalog():
    # Đọc thư mục thực tế để hiển thị đủ API ngay cả khi manifest chưa cập nhật.
    return [info_for(d.name) for d in sorted(API_ROOT.iterdir())
            if d.is_dir() and not d.name.startswith("_") and (d / "meta.yaml").is_file()]


@app.get("/api/items/{api_id}")
def api_detail(api_id: str):
    return {"info": info_for(api_id), "spec": spec_for(api_id)}


@app.get("/specs/{api_id}.json")
def api_spec(api_id: str):
    return spec_for(api_id)


@app.get("/documents/{api_id}/{kind}", response_class=PlainTextResponse)
def api_document(api_id: str, kind: str):
    directory = api_dir(api_id)
    if kind not in ("original", "rendered", "ablated"):
        raise HTTPException(404, "Không tìm thấy tài liệu")
    relative = read_yaml(directory / "meta.yaml")["docs"].get(kind)
    if not relative:
        raise HTTPException(404, "API này chưa có tài liệu được chọn")
    path = (directory / relative).resolve()
    if not path.is_relative_to(directory.resolve()) or not path.is_file():
        raise HTTPException(404, "Không tìm thấy tài liệu")
    return path.read_text(encoding="utf-8")


@app.get("/swagger/{api_id}", include_in_schema=False)
def swagger(api_id: str):
    api_dir(api_id)
    return get_swagger_ui_html(openapi_url=f"/specs/{api_id}.json", title=f"{api_id} · Swagger",
                               swagger_ui_parameters={"supportedSubmitMethods": []})


if __name__ == "__main__":
    import uvicorn

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    print(f"Mo trinh duyet: http://127.0.0.1:{args.port}", flush=True)
    uvicorn.run(app, host="127.0.0.1", port=args.port)
