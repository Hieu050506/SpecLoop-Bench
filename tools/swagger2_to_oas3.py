"""Chuyển một đặc tả Swagger 2.0 sang OpenAPI 3.0.3 (không cần Node.js).

Xử lý: host/basePath/schemes -> servers; tham số body/formData -> requestBody; consumes/produces -> content;
definitions -> components/schemas; securityDefinitions -> components/securitySchemes; kiểu dữ liệu của
tham số -> schema; collectionFormat -> style/explode; response.schema/headers -> content/headers.

Dùng:  python tools/swagger2_to_oas3.py swagger.json -o openapi.yaml
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from oas_utils import HTTP_METHODS, dump_yaml, validate_spec  # noqa: E402

SCHEMA_KEYS = ("type", "format", "items", "enum", "default", "minimum", "maximum", "exclusiveMinimum",
               "exclusiveMaximum", "minLength", "maxLength", "pattern", "minItems", "maxItems", "uniqueItems",
               "multipleOf")
COLLECTION_FORMATS = {"csv": ("form", False), "ssv": ("spaceDelimited", False), "pipes": ("pipeDelimited", False),
                      "multi": ("form", True)}


def _fix_refs(node):
    if isinstance(node, dict):
        return {k: (v.replace("#/definitions/", "#/components/schemas/") if k == "$ref" and isinstance(v, str)
                    else _fix_refs(v)) for k, v in node.items()}
    if isinstance(node, list):
        return [_fix_refs(x) for x in node]
    return node


def _param_schema(p: dict) -> dict:
    if p.get("type") == "file":
        return {"type": "string", "format": "binary"}
    sch = {k: p[k] for k in SCHEMA_KEYS if k in p}
    if "schema" in p and not sch:
        sch = p["schema"]
    return sch


def _convert_param(p: dict) -> dict:
    q = {k: p[k] for k in ("name", "in", "description", "required", "deprecated") if k in p}
    if p.get("in") == "path":
        q["required"] = True
    q["schema"] = _param_schema(p)
    if p.get("allowEmptyValue"):
        q["allowEmptyValue"] = True
    if p.get("type") == "array" and p.get("collectionFormat"):
        style, explode = COLLECTION_FORMATS.get(p["collectionFormat"], ("form", True))
        q["style"], q["explode"] = style, explode
    return q


def _convert_params(params, default_consumes):
    new_params, body, form = [], None, []
    for p in params or []:
        if p.get("in") == "body":
            body = p
        elif p.get("in") == "formData":
            form.append(p)
        else:
            new_params.append(_convert_param(p))
    rb = None
    if body is not None:
        rb = {"content": {m: {"schema": body.get("schema", {})} for m in default_consumes}}
        if body.get("description"):
            rb["description"] = body["description"]
        if body.get("required"):
            rb["required"] = True
    elif form:
        props, req = {}, []
        for p in form:
            props[p["name"]] = _param_schema(p)
            if p.get("description"):
                props[p["name"]]["description"] = p["description"]
            if p.get("required"):
                req.append(p["name"])
        sch = {"type": "object", "properties": props}
        if req:
            sch["required"] = req
        media = [m for m in default_consumes if "form" in m]
        if not media:
            media = ["multipart/form-data" if any(p.get("type") == "file" for p in form) else "application/x-www-form-urlencoded"]
        rb = {"content": {m: {"schema": sch} for m in media}}
    return new_params, rb


INFO_KEYS = {"title", "description", "termsOfService", "contact", "license", "version"}
CONTACT_KEYS = {"name", "url", "email"}
LICENSE_KEYS = {"name", "url"}


def _x_prefix_unknown(obj: dict, known: set) -> dict:
    """Trường ngoài chuẩn (vd. Flasgger thêm responsibleOrganization) -> tiền tố x- để hợp lệ OAS 3.0."""
    return {(k if k in known or k.startswith("x-") else f"x-{k}"): v for k, v in obj.items()}


def convert(src: dict) -> dict:
    src = copy.deepcopy(src)
    info = dict(src.get("info") or {"title": "API", "version": "1.0.0"})
    for key, known in (("contact", CONTACT_KEYS), ("license", LICENSE_KEYS)):
        if isinstance(info.get(key), dict):
            info[key] = _x_prefix_unknown(info[key], known)
    out: dict = {"openapi": "3.0.3", "info": _x_prefix_unknown(info, INFO_KEYS)}
    host, base = src.get("host"), src.get("basePath") or ""
    if host:
        scheme = (src.get("schemes") or ["https"])[0]
        out["servers"] = [{"url": f"{scheme}://{host}{base.rstrip('/')}"}]
    elif base and base != "/":
        out["servers"] = [{"url": base.rstrip("/")}]
    if src.get("tags"):
        out["tags"] = src["tags"]
    if src.get("externalDocs"):
        out["externalDocs"] = src["externalDocs"]
    g_consumes = src.get("consumes") or ["application/json"]
    g_produces = src.get("produces") or ["application/json"]
    paths = {}
    for path, item in (src.get("paths") or {}).items():
        new_item = {}
        shared_params, shared_rb = _convert_params(item.get("parameters"), g_consumes)
        if shared_params:
            new_item["parameters"] = shared_params
        for k, v in item.items():
            if k == "parameters":
                continue
            if k not in HTTP_METHODS or not isinstance(v, dict):
                new_item[k] = v
                continue
            op = dict(v)
            consumes = op.pop("consumes", None) or g_consumes
            produces = op.pop("produces", None) or g_produces
            params, rb = _convert_params(op.get("parameters"), consumes)
            op.pop("parameters", None)
            if params:
                op["parameters"] = params
            rb = rb or shared_rb
            if rb:
                op["requestBody"] = rb
            resps = {}
            for code, r in (op.get("responses") or {}).items():
                r = dict(r) if isinstance(r, dict) else {"description": str(r)}
                sch = r.pop("schema", None)
                if sch is not None:
                    r["content"] = {m: {"schema": sch} for m in produces}
                if isinstance(r.get("headers"), dict):
                    r["headers"] = {hn: {**({"description": hv["description"]} if hv.get("description") else {}),
                                         "schema": _param_schema(hv)} for hn, hv in r["headers"].items()}
                r.setdefault("description", f"Response {code}")
                resps[str(code)] = r
            op["responses"] = resps or {"default": {"description": "Default response"}}
            new_item[k] = op
        paths[path] = new_item
    out["paths"] = paths
    comps = {}
    if src.get("definitions"):
        comps["schemas"] = src["definitions"]
    if src.get("securityDefinitions"):
        schemes = {}
        for name, sd in src["securityDefinitions"].items():
            t = sd.get("type")
            if t == "basic":
                schemes[name] = {"type": "http", "scheme": "basic"}
            elif t == "apiKey":
                schemes[name] = {"type": "apiKey", "in": sd.get("in", "header"), "name": sd.get("name", "X-API-Key")}
            elif t == "oauth2":
                flow = {"implicit": "implicit", "password": "password", "application": "clientCredentials",
                        "accessCode": "authorizationCode"}.get(sd.get("flow"), "implicit")
                f = {k: sd[k] for k in ("authorizationUrl", "tokenUrl") if k in sd}
                f["scopes"] = sd.get("scopes") or {}
                schemes[name] = {"type": "oauth2", "flows": {flow: f}}
            if sd.get("description") and name in schemes:
                schemes[name]["description"] = sd["description"]
        comps["securitySchemes"] = schemes
    if comps:
        out["components"] = comps
    if src.get("security"):
        out["security"] = src["security"]
    return _fix_refs(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src")
    ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    text = Path(a.src).read_text(encoding="utf-8")
    src = json.loads(text) if text.lstrip().startswith("{") else yaml.safe_load(text)
    if str(src.get("swagger")) != "2.0":
        sys.exit("Đầu vào không phải Swagger 2.0")
    out = convert(src)
    errs = validate_spec(out)
    dump_yaml(out, a.out)
    print(f"Đã ghi {a.out}: {len(out['paths'])} path; " + ("hợp lệ OAS 3.0.3" if not errs else f"CẢNH BÁO: {errs}"))


if __name__ == "__main__":
    main()
