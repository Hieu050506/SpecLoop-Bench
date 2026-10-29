"""Phân rã một đặc tả OpenAPI thành các atomic facts dùng để chấm điểm.

Nhóm fact (category):
  endpoint        (METHOD, path chuẩn hóa)
  parameter       (operation, in, name)
  request_body    (operation, media type)
  request_field   (operation, đường dẫn thuộc tính trong body)
  response        (operation, status)
  response_field  (operation, status, đường dẫn thuộc tính)
  constraint      (operation, vị trí, từ khóa) = giá trị

Dùng:  python tools/extract_facts.py apis/bookstore-lab/ground_truth/openapi.yaml [-o facts.jsonl]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from oas_utils import deref, iter_operations, load_spec, merged_parameters, norm_path, server_base_path  # noqa: E402

CONSTRAINT_KEYWORDS = (
    "type", "format", "enum", "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum",
    "minLength", "maxLength", "pattern", "minItems", "maxItems", "uniqueItems", "multipleOf",
    "default", "nullable",
)
# Ràng buộc "đầu vào" có thể dò bằng probe – dùng cho biến thể tài liệu lược ràng buộc
PROBEABLE = {"enum", "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "minLength",
             "maxLength", "pattern", "minItems", "maxItems", "uniqueItems", "multipleOf", "required"}
MAX_REQ_DEPTH = 4
MAX_RESP_DEPTH = 3


def norm_value(kw, v):
    if kw == "enum" and isinstance(v, list):
        return sorted({json.dumps(x, ensure_ascii=False) if not isinstance(x, str) else x for x in v})
    if isinstance(v, bool):
        return v
    if isinstance(v, float) and v.is_integer():
        return int(v)
    return v


def _fid(key: str) -> str:
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


class FactSink:
    def __init__(self):
        self.facts: dict[str, dict] = {}

    def add(self, category, op, location=None, name=None, keyword=None, value=None, **extra):
        parts = [category, op or "", location or "", name or "", keyword or ""]
        key = "|".join(parts)
        if key in self.facts:
            return
        rec = {"id": _fid(key), "category": category, "op": op, "location": location, "name": name}
        if keyword is not None:
            rec["keyword"] = keyword
            rec["value"] = norm_value(keyword, value)
        rec.update(extra)
        rec["key"] = key
        self.facts[key] = rec


def _schema_type(s: dict):
    if not isinstance(s, dict):
        return None
    if "type" in s:
        return s["type"]
    if "properties" in s:
        return "object"
    if "items" in s:
        return "array"
    return None


def _merge_allof(s: dict) -> dict:
    if not isinstance(s, dict) or "allOf" not in s:
        return s
    out = {k: v for k, v in s.items() if k != "allOf"}
    props, req = dict(out.get("properties", {})), list(out.get("required", []))
    for part in s["allOf"]:
        part = _merge_allof(part)
        if not isinstance(part, dict):
            continue
        props.update(part.get("properties", {}))
        req += part.get("required", [])
        for k, v in part.items():
            if k not in ("properties", "required") and k not in out:
                out[k] = v
    if props:
        out["properties"] = props
    if req:
        out["required"] = sorted(set(req))
    return out


def emit_schema_constraints(sink, op, location, name, s, skip=()):
    s = _merge_allof(s)
    if not isinstance(s, dict):
        return
    t = _schema_type(s)
    if t is not None:
        sink.add("constraint", op, location, name, "type", t)
    for kw in CONSTRAINT_KEYWORDS:
        if kw == "type" or kw in skip:
            continue
        if kw in s and not (kw in ("exclusiveMinimum", "exclusiveMaximum", "uniqueItems", "nullable") and s[kw] is False):
            sink.add("constraint", op, location, name, kw, s[kw])


def walk_fields(sink, op, category, loc_prefix, s, path="", depth=0, max_depth=3, parent_required=()):
    """Duyệt thuộc tính object/array, sinh fact field + ràng buộc."""
    s = _merge_allof(s)
    if not isinstance(s, dict) or depth > max_depth or "x-cycle" in s:
        return
    if _schema_type(s) == "array" and isinstance(s.get("items"), dict):
        walk_fields(sink, op, category, loc_prefix, s["items"], path + "[]", depth + 1, max_depth)
        return
    branches = [s]
    for comb in ("oneOf", "anyOf"):
        if isinstance(s.get(comb), list):
            branches += [_merge_allof(b) for b in s[comb] if isinstance(b, dict)]
    for b in branches:
        props = b.get("properties") or {}
        req = set(b.get("required") or [])
        for pname, ps in props.items():
            ps = _merge_allof(ps)
            fpath = f"{path}.{pname}" if path else pname
            sink.add(category, op, loc_prefix, fpath)
            loc = f"{loc_prefix}:{fpath}"
            if pname in req:
                sink.add("constraint", op, loc, fpath, "required", True)
            emit_schema_constraints(sink, op, loc, fpath, ps)
            walk_fields(sink, op, category, loc_prefix, ps, fpath, depth + 1, max_depth)


def extract(spec: dict) -> list[dict]:
    sink = FactSink()
    base = server_base_path(spec)
    for method, path, op, item in iter_operations(spec):
        opk = f"{method} {norm_path(path, base)}"
        sink.add("endpoint", opk, raw_path=path)
        # tham số
        for p in merged_parameters(spec, op, item):
            loc = f"{p.get('in')}:{p['name']}"
            sink.add("parameter", opk, p.get("in"), p["name"])
            if p.get("required") or p.get("in") == "path":
                sink.add("constraint", opk, loc, p["name"], "required", True)
            sch = deref(spec, p.get("schema") or {})
            emit_schema_constraints(sink, opk, loc, p["name"], sch)
            walk_fields(sink, opk, "request_field", f"{p.get('in')}:{p['name']}", sch, max_depth=2)
        # body
        rb = deref(spec, op.get("requestBody") or {})
        for media, mobj in (rb.get("content") or {}).items():
            sink.add("request_body", opk, "body", media)
            if rb.get("required"):
                sink.add("constraint", opk, "body", media, "required", True)
            sch = (mobj or {}).get("schema") or {}
            if _schema_type(_merge_allof(sch)) not in (None, "object", "array"):
                emit_schema_constraints(sink, opk, "body", media, sch)
            walk_fields(sink, opk, "request_field", "body", sch, max_depth=MAX_REQ_DEPTH)
            break  # chỉ lấy media type đầu tiên để tránh trùng lặp
        # x-dependencies (phụ thuộc giữa tham số)
        for dep in op.get("x-dependencies") or []:
            sink.add("constraint", opk, "operation", "x-dependencies", "dependency", " ".join(str(dep).split()))
        # response
        for status, resp in (op.get("responses") or {}).items():
            status = str(status)
            resp = deref(spec, resp)
            sink.add("response", opk, status)
            for media, mobj in ((resp or {}).get("content") or {}).items():
                sch = (mobj or {}).get("schema") or {}
                walk_fields(sink, opk, "response_field", f"resp{status}", sch, max_depth=MAX_RESP_DEPTH)
                break
    return list(sink.facts.values())


def write_jsonl(facts, path):
    with open(path, "w", encoding="utf-8") as f:
        for r in sorted(facts, key=lambda r: r["key"]):
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def read_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def summarize(facts):
    out = {}
    for r in facts:
        out[r["category"]] = out.get(r["category"], 0) + 1
    kws = {}
    for r in facts:
        if r["category"] == "constraint":
            kws[r["keyword"]] = kws.get(r["keyword"], 0) + 1
    out["constraint_by_keyword"] = dict(sorted(kws.items(), key=lambda x: -x[1]))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    facts = extract(load_spec(a.spec))
    if a.out:
        write_jsonl(facts, a.out)
        print(f"Đã ghi {len(facts)} facts -> {a.out}")
    print(json.dumps(summarize(facts), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
