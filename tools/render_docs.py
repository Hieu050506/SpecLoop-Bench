"""Sinh tài liệu API dạng Markdown (giống trang Swagger UI/Redoc) từ một đặc tả OpenAPI.

Tài liệu sinh ra là ĐẦU VÀO cho hệ thống (LLM đọc tài liệu -> sinh OAS). Có thể ẩn một tập
ràng buộc (biến thể "ablated") để đo khả năng phục hồi ràng buộc nhờ phản hồi kiểm thử.

Dùng:
  python tools/render_docs.py spec.yaml -o docs/rendered.md
  python tools/render_docs.py spec.yaml -o docs/ablated.md --hide ground_truth/ablation.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from oas_utils import deref, iter_operations, load_spec, merged_parameters, norm_path, server_base_path  # noqa: E402
from extract_facts import _merge_allof, _schema_type  # noqa: E402

MAX_DEPTH = 3
CONSTRAINT_WORDS = re.compile(
    r"\b(max(imum)?|min(imum)?|at (most|least)|between|up to|no more than|no less than|must be one of|"
    r"one of|allowed values?|default(s)?( to)?|length|characters|pattern|greater|less|range|limit(ed)?)\b",
    re.IGNORECASE)


class Hider:
    def __init__(self, keys=None):
        self.keys = set(keys or [])
        self.used = set()

    def hidden(self, op, loc, name, kw):
        k = f"constraint|{op}|{loc}|{name}|{kw}"
        if k in self.keys:
            self.used.add(k)
            return True
        return False

    def any_hidden(self, op, loc, name):
        return any(k.startswith(f"constraint|{op}|{loc}|{name}|") for k in self.keys)


def _fmt(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (dict, list)):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def _join(desc: str, ctext: str) -> str:
    if desc and ctext and desc[-1] not in ".!?:;":
        desc += "."
    return " ".join(x for x in (desc, ctext) if x)


def type_label(s: dict) -> str:
    s = _merge_allof(s) or {}
    t = _schema_type(s)
    if t == "array":
        inner = type_label(s.get("items") or {})
        return f"array of {inner}" if inner else "array"
    if t is None:
        if "oneOf" in s or "anyOf" in s:
            return "one of several types"
        return "any"
    if s.get("format"):
        return f"{t} ({s['format']})"
    return t


def constraint_text(s: dict, op, loc, name, hider: Hider) -> str:
    s = _merge_allof(s) or {}
    bits = []

    def show(kw):
        return kw in s and not hider.hidden(op, loc, name, kw)

    if show("enum"):
        bits.append("Allowed values: " + ", ".join(f"`{_fmt(x)}`" for x in s["enum"]) + ".")
    if show("default"):
        bits.append(f"Default: `{_fmt(s['default'])}`.")
    excl_min = s.get("exclusiveMinimum") is True and not hider.hidden(op, loc, name, "exclusiveMinimum")
    excl_max = s.get("exclusiveMaximum") is True and not hider.hidden(op, loc, name, "exclusiveMaximum")
    if show("minimum"):
        bits.append(("Must be greater than " if excl_min else "Minimum: ") + f"{_fmt(s['minimum'])}.")
    if show("maximum"):
        bits.append(("Must be less than " if excl_max else "Maximum: ") + f"{_fmt(s['maximum'])}.")
    if show("minLength"):
        bits.append(f"Min length: {s['minLength']}.")
    if show("maxLength"):
        bits.append(f"Max length: {s['maxLength']}.")
    if show("pattern"):
        bits.append(f"Pattern: `{s['pattern']}`.")
    if show("minItems"):
        bits.append(f"Min items: {s['minItems']}.")
    if show("maxItems"):
        bits.append(f"Max items: {s['maxItems']}.")
    if s.get("uniqueItems") is True and not hider.hidden(op, loc, name, "uniqueItems"):
        bits.append("Items must be unique.")
    if show("multipleOf"):
        bits.append(f"Multiple of {s['multipleOf']}.")
    if s.get("nullable") is True and not hider.hidden(op, loc, name, "nullable"):
        bits.append("May be null.")
    return " ".join(bits)


def clean_desc(text: str | None, scrub: bool) -> str:
    if not text:
        return ""
    text = " ".join(str(text).split())
    if scrub:
        sentences = re.split(r"(?<=[.!?])\s+", text)
        text = " ".join(x for x in sentences if not (CONSTRAINT_WORDS.search(x) or re.search(r"\d", x)))
    return text.replace("|", "\\|")


def render_fields(lines, s, op, loc_prefix, hider, path="", depth=0, indent=""):
    s = _merge_allof(s)
    if not isinstance(s, dict) or depth > MAX_DEPTH or "x-cycle" in s:
        return
    if _schema_type(s) == "array" and isinstance(s.get("items"), dict):
        render_fields(lines, s["items"], op, loc_prefix, hider, path + "[]", depth, indent)
        return
    branches = [s] + [_merge_allof(b) for c in ("oneOf", "anyOf") for b in (s.get(c) or []) if isinstance(b, dict)]
    for b in branches:
        req = set(b.get("required") or [])
        for pname, ps in (b.get("properties") or {}).items():
            ps = _merge_allof(ps) or {}
            fpath = f"{path}.{pname}" if path else pname
            loc = f"{loc_prefix}:{fpath}"
            is_req = pname in req and not hider.hidden(op, loc, fpath, "required")
            scrub = hider.any_hidden(op, loc, fpath)
            desc = clean_desc(ps.get("description"), scrub)
            ctext = constraint_text(ps, op, loc, fpath, hider)
            label = type_label(ps)
            line = f"{indent}- `{pname}` ({label}{', required' if is_req else ''})"
            rest = _join(desc, ctext)
            lines.append(line + (f" — {rest}" if rest else ""))
            render_fields(lines, ps, op, loc_prefix, hider, fpath, depth + 1, indent + "  ")


def render(spec: dict, hide_keys=None, title_suffix="") -> tuple[str, set]:
    hider = Hider(hide_keys)
    info = spec.get("info", {})
    base = server_base_path(spec)
    L = [f"# {info.get('title', 'API')} — API Reference{title_suffix}", ""]
    if info.get("description"):
        L += [str(info["description"]).strip(), ""]
    if info.get("version"):
        L.append(f"**Version:** {info['version']}  ")
    servers = spec.get("servers") or []
    if servers:
        L.append(f"**Base URL:** `{servers[0].get('url')}`")
    L.append("")
    sec = (spec.get("components") or {}).get("securitySchemes") or {}
    if sec:
        L += ["## Authentication", ""]
        for name, sch in sec.items():
            sch = deref(spec, sch)
            t = sch.get("type")
            if t == "apiKey":
                L.append(f"- **{name}**: API key sent in {sch.get('in')} parameter `{sch.get('name')}`.")
            elif t == "http":
                L.append(f"- **{name}**: HTTP {sch.get('scheme', '')} authentication"
                         + (f" ({sch.get('bearerFormat')})" if sch.get("bearerFormat") else "") + ".")
            else:
                L.append(f"- **{name}**: {t}.")
            if sch.get("description"):
                L.append(f"  {clean_desc(sch['description'], False)}")
        L.append("")
    # gom theo tag
    groups: dict[str, list] = {}
    for method, path, op, item in iter_operations(spec):
        tag = (op.get("tags") or ["Endpoints"])[0]
        groups.setdefault(tag, []).append((method, path, op, item))
    tag_desc = {t.get("name"): t.get("description") for t in spec.get("tags") or [] if isinstance(t, dict)}
    for tag, ops in groups.items():
        L += [f"## {tag}", ""]
        if tag_desc.get(tag):
            L += [clean_desc(tag_desc[tag], False), ""]
        for method, path, op, item in ops:
            opk = f"{method} {norm_path(path, base)}"
            L += [f"### {method} {path}", ""]
            if op.get("summary"):
                L += [f"**{clean_desc(op['summary'], False)}**", ""]
            if op.get("description"):
                L += [str(op["description"]).strip(), ""]
            if op.get("deprecated"):
                L += ["> Deprecated.", ""]
            params = merged_parameters(spec, op, item)
            if params:
                L += ["**Parameters**", "", "| Name | In | Type | Required | Description |", "|---|---|---|---|---|"]
                for p in params:
                    loc = f"{p.get('in')}:{p['name']}"
                    sch = deref(spec, p.get("schema") or {})
                    req = (p.get("required") or p.get("in") == "path") and not (
                        p.get("in") != "path" and hider.hidden(opk, loc, p["name"], "required"))
                    scrub = hider.any_hidden(opk, loc, p["name"])
                    desc = _join(clean_desc(p.get("description"), scrub), constraint_text(sch, opk, loc, p["name"], hider))
                    L.append(f"| `{p['name']}` | {p.get('in')} | {type_label(sch)} | {'Yes' if req else 'No'} | {desc} |")
                L.append("")
            deps = op.get("x-dependencies") or []
            shown = [d for d in deps if not hider.hidden(opk, "operation", "x-dependencies", "dependency")]
            if shown:
                L += ["**Parameter dependencies:** " + "; ".join(f"`{d}`" for d in shown), ""]
            rb = deref(spec, op.get("requestBody") or {})
            for media, mobj in (rb.get("content") or {}).items():
                sch = (mobj or {}).get("schema") or {}
                L += [f"**Request body** (`{media}`{', required' if rb.get('required') else ''})", ""]
                if rb.get("description"):
                    L += [clean_desc(rb["description"], False), ""]
                lines: list[str] = []
                render_fields(lines, sch, opk, "body", hider)
                if not lines:
                    L.append(f"- Body type: {type_label(sch)}")
                L += lines + [""]
                ex = (mobj or {}).get("example") or sch.get("example") if isinstance(sch, dict) else None
                if ex is not None:
                    L += ["Example:", "", "```json", json.dumps(ex, ensure_ascii=False, indent=2), "```", ""]
                break
            resps = op.get("responses") or {}
            if resps:
                L += ["**Responses**", ""]
                for status, resp in resps.items():
                    resp = deref(spec, resp) or {}
                    L.append(f"- **{status}** — {clean_desc(resp.get('description'), False) or 'Response'}")
                    for media, mobj in (resp.get("content") or {}).items():
                        sch = (mobj or {}).get("schema") or {}
                        lines = []
                        render_fields(lines, sch, opk, f"resp{status}", hider, indent="  ")
                        if lines:
                            L.append(f"  Body (`{media}`, {type_label(sch)}):")
                            L += lines
                        break
                L.append("")
    return "\n".join(L).rstrip() + "\n", hider.used


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--hide", help="ablation.json chứa danh sách khóa ràng buộc cần ẩn")
    a = ap.parse_args()
    keys = json.load(open(a.hide, encoding="utf-8"))["hidden_keys"] if a.hide else None
    text, used = render(load_spec(a.spec), keys)
    Path(a.out).write_text(text, encoding="utf-8")
    print(f"Đã ghi {a.out} ({len(text.splitlines())} dòng; ẩn {len(used)} ràng buộc)")


if __name__ == "__main__":
    main()
