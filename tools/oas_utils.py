"""Tiện ích dùng chung cho bộ dữ liệu SpecLoop-Bench: đọc/ghi OpenAPI, phân giải $ref,
hạ cấp 3.1 -> 3.0.3, kiểm tra hợp lệ, duyệt operation."""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import yaml

HTTP_METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")
TARGET_VERSION = "3.0.3"


# ----------------------------------------------------------------- đọc / ghi
def load_spec(path: str | Path) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    if str(path).endswith(".json"):
        return json.loads(text)
    return yaml.safe_load(text)


class _Dumper(yaml.SafeDumper):
    pass


def _str_presenter(dumper, data):
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_Dumper.add_representer(str, _str_presenter)


def dump_yaml(data, path: str | Path | None = None) -> str:
    text = yaml.dump(data, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=110)
    if path is not None:
        Path(path).write_text(text, encoding="utf-8")
    return text


def sha256_file(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# ----------------------------------------------------------------- $ref
def resolve_pointer(spec: dict, ref: str):
    if not ref.startswith("#/"):
        raise ValueError(f"Chỉ hỗ trợ $ref nội bộ, gặp: {ref}")
    node = spec
    for part in ref[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        node = node[part]
    return node


def deref(spec: dict, node, _stack: tuple = (), max_depth: int = 12):
    """Trả về bản sao đã thay mọi $ref nội bộ bằng nội dung; vòng lặp được đánh dấu x-cycle."""
    if len(_stack) > max_depth:
        return {"x-truncated": True}
    if isinstance(node, dict):
        if "$ref" in node and isinstance(node["$ref"], str):
            ref = node["$ref"]
            if ref in _stack:
                return {"x-cycle": ref}
            target = resolve_pointer(spec, ref)
            merged = deref(spec, target, _stack + (ref,), max_depth)
            siblings = {k: v for k, v in node.items() if k != "$ref"}
            if siblings and isinstance(merged, dict):
                merged = {**merged, **deref(spec, siblings, _stack, max_depth)}
            return merged
        return {k: deref(spec, v, _stack, max_depth) for k, v in node.items()}
    if isinstance(node, list):
        return [deref(spec, v, _stack, max_depth) for v in node]
    return node


# ----------------------------------------------------------------- chuẩn hóa phiên bản
def _downgrade_schema(s):
    """Chuyển một schema JSON Schema 2020-12 (OAS 3.1) về dạng OAS 3.0."""
    if isinstance(s, list):
        return [_downgrade_schema(x) for x in s]
    if not isinstance(s, dict):
        return s
    s = {k: _downgrade_schema(v) for k, v in s.items()}
    t = s.get("type")
    if isinstance(t, list):
        types = [x for x in t if x != "null"]
        if "null" in t:
            s["nullable"] = True
        s["type"] = types[0] if len(types) == 1 else (types[0] if types else "string")
    for kw, base in (("exclusiveMinimum", "minimum"), ("exclusiveMaximum", "maximum")):
        if kw in s and not isinstance(s[kw], bool):
            s[base] = s[kw]
            s[kw] = True
    if "const" in s:
        s["enum"] = [s.pop("const")]
    if "examples" in s and isinstance(s["examples"], list):
        ex = s.pop("examples")
        if ex and "example" not in s:
            s["example"] = ex[0]
    for k in ("$schema", "$id", "contentMediaType", "contentEncoding", "$comment"):
        s.pop(k, None)
    # oneOf [X, {type: null}] -> X + nullable
    for comb in ("oneOf", "anyOf"):
        if comb in s and isinstance(s[comb], list):
            non_null = [x for x in s[comb] if not (isinstance(x, dict) and x.get("type") == "null")]
            if len(non_null) < len(s[comb]):
                s["nullable"] = True
                if len(non_null) == 1:
                    inner = s.pop(comb)
                    inner = non_null[0]
                    if "$ref" in inner:
                        s["allOf"] = [inner]
                    else:
                        s.update(inner)
                else:
                    s[comb] = non_null
    return s


def _walk_schemas(node, fn, key=None):
    """Áp dụng fn lên mọi giá trị nằm dưới khóa 'schema' / 'schemas'."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k == "schema":
                out[k] = fn(v)
            elif k == "schemas" and isinstance(v, dict):
                out[k] = {name: fn(sch) for name, sch in v.items()}
            else:
                out[k] = _walk_schemas(v, fn, k)
        return out
    if isinstance(node, list):
        return [_walk_schemas(x, fn, key) for x in node]
    return node


def normalize_to_303(spec: dict) -> tuple[dict, list[str]]:
    """Đưa đặc tả về OpenAPI 3.0.3. Trả về (spec_mới, danh_sách_ghi_chú)."""
    notes: list[str] = []
    spec = copy.deepcopy(spec)
    if "swagger" in spec:
        raise ValueError("Đặc tả là Swagger 2.0. Hãy chuyển sang OpenAPI 3 trước (xem README, mục Thêm API).")
    ver = str(spec.get("openapi", ""))
    if ver.startswith("3.1"):
        spec = _walk_schemas(spec, _downgrade_schema)
        for k in ("jsonSchemaDialect", "webhooks"):
            if spec.pop(k, None) is not None:
                notes.append(f"bỏ trường '{k}' (chỉ có ở 3.1)")
        info = spec.get("info", {})
        if "summary" in info:
            info.pop("summary")
            notes.append("bỏ info.summary (chỉ có ở 3.1)")
        lic = info.get("license", {})
        if isinstance(lic, dict) and "identifier" in lic:
            lic.pop("identifier")
            notes.append("bỏ license.identifier (chỉ có ở 3.1)")
        notes.append(f"hạ cấp OpenAPI {ver} -> {TARGET_VERSION} (type null -> nullable, exclusive* số -> boolean, const -> enum, examples -> example)")
    elif ver.startswith("3.0"):
        if ver != TARGET_VERSION:
            notes.append(f"đổi nhãn phiên bản {ver} -> {TARGET_VERSION} (tương thích ngữ nghĩa)")
    else:
        raise ValueError(f"Không nhận ra phiên bản OpenAPI: {ver!r}")
    spec["openapi"] = TARGET_VERSION
    if not spec.get("paths"):
        raise ValueError("Đặc tả không có 'paths'.")
    # Mã phản hồi viết dạng số (200:) -> chuỗi ('200':) theo chuẩn
    fixed = 0
    for item in spec["paths"].values():
        if not isinstance(item, dict):
            continue
        for m in HTTP_METHODS:
            op = item.get(m)
            if isinstance(op, dict) and isinstance(op.get("responses"), dict):
                if any(not isinstance(k, str) for k in op["responses"]):
                    op["responses"] = {str(k): v for k, v in op["responses"].items()}
                    fixed += 1
    if fixed:
        notes.append(f"chuyển mã phản hồi dạng số sang chuỗi ở {fixed} operation")
    return spec, notes


def validate_spec(spec: dict) -> list[str]:
    """Trả về danh sách lỗi (rỗng nếu hợp lệ OAS 3.0)."""
    try:
        from openapi_spec_validator import validate
        from openapi_spec_validator.validation.exceptions import OpenAPIValidationError  # noqa: F401
    except ImportError:  # pragma: no cover
        return ["Chưa cài openapi-spec-validator (pip install -r tools/requirements.txt)"]
    try:
        validate(spec)
        return []
    except Exception as e:  # noqa: BLE001
        msg = str(e).split("\n")[0]
        return [msg[:400]]


# ----------------------------------------------------------------- operation
def server_base_path(spec: dict) -> str:
    servers = spec.get("servers") or []
    if not servers:
        return ""
    url = servers[0].get("url", "")
    path = urlparse(url).path if "://" in url else url
    path = re.sub(r"\{[^}]+\}", "", path)
    return path.rstrip("/")


def norm_path(path: str, base: str = "") -> str:
    full = (base.rstrip("/") + "/" + path.lstrip("/")) if base else path
    full = re.sub(r"\{[^}]+\}", "{}", full)
    full = re.sub(r"/+", "/", full)
    if len(full) > 1:
        full = full.rstrip("/")
    return full


def iter_operations(spec: dict):
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for method in HTTP_METHODS:
            if method in item and isinstance(item[method], dict):
                yield method.upper(), path, item[method], item


def merged_parameters(spec: dict, op: dict, path_item: dict) -> list[dict]:
    params: dict[tuple, dict] = {}
    for p in (path_item.get("parameters") or []) + (op.get("parameters") or []):
        p = deref(spec, p)
        if not isinstance(p, dict) or "name" not in p:
            continue
        params[(p.get("in"), p["name"])] = p
    return list(params.values())
