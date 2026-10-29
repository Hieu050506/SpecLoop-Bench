"""Chấm điểm một đặc tả sinh ra (pred) so với ground truth theo atomic facts.

- endpoint/parameter/request_body/request_field/response/response_field: khớp theo khóa.
- constraint: khớp khi cùng khóa (operation, vị trí, từ khóa) VÀ cùng giá trị.
  Fact đúng khóa nhưng sai giá trị được tính là FP + FN và liệt kê riêng ("sai giá trị").
- Đường dẫn được chuẩn hóa: ghép base path của servers, bỏ tên biến ({id} == {bookId}).

Dùng:
  python tools/evaluate.py --gt apis/bookstore-lab/ground_truth/openapi.yaml --pred my_generated.yaml
  python tools/evaluate.py --api bookstore-lab --pred my_generated.yaml --gt-kind behavior --report out.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_facts import extract  # noqa: E402
from oas_utils import load_spec  # noqa: E402

CATS = ["endpoint", "parameter", "request_body", "request_field", "response", "response_field", "constraint"]


def _prf(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return round(p, 4), round(r, 4), round(f, 4)


def _ckey(f):  # khóa không kèm giá trị
    return f["key"]


def compare(gt_facts, pred_facts, keywords=None):
    res = {"by_category": {}, "constraint_by_keyword": {}, "wrong_value": [], "fp": [], "fn": []}
    gt = {_ckey(f): f for f in gt_facts}
    pr = {_ckey(f): f for f in pred_facts}
    if keywords:
        gt = {k: v for k, v in gt.items() if v["category"] != "constraint" or v["keyword"] in keywords}
        pr = {k: v for k, v in pr.items() if v["category"] != "constraint" or v["keyword"] in keywords}
    totals = {"tp": 0, "fp": 0, "fn": 0}
    kw_stats: dict[str, dict] = {}
    for cat in CATS:
        g = {k for k, v in gt.items() if v["category"] == cat}
        p = {k for k, v in pr.items() if v["category"] == cat}
        both = g & p
        if cat == "constraint":
            ok = {k for k in both if gt[k]["value"] == pr[k]["value"]}
            wrong = both - ok
            for k in wrong:
                res["wrong_value"].append({"key": k, "gt": gt[k]["value"], "pred": pr[k]["value"]})
            tp, fp, fn = len(ok), len(p - g) + len(wrong), len(g - p) + len(wrong)
            for k in g | p:
                kw = (gt.get(k) or pr.get(k))["keyword"]
                st = kw_stats.setdefault(kw, {"tp": 0, "fp": 0, "fn": 0})
                if k in ok:
                    st["tp"] += 1
                else:
                    if k in p:
                        st["fp"] += 1
                    if k in g:
                        st["fn"] += 1
        else:
            tp, fp, fn = len(both), len(p - g), len(g - p)
        res["fp"] += sorted(p - g)
        res["fn"] += sorted(g - p)
        P, R, F = _prf(tp, fp, fn)
        res["by_category"][cat] = {"gt": len(g), "pred": len(p), "tp": tp, "fp": fp, "fn": fn,
                                   "precision": P, "recall": R, "f1": F}
        for k in totals:
            totals[k] += {"tp": tp, "fp": fp, "fn": fn}[k]
    for kw, st in sorted(kw_stats.items()):
        P, R, F = _prf(st["tp"], st["fp"], st["fn"])
        res["constraint_by_keyword"][kw] = {**st, "precision": P, "recall": R, "f1": F}
    P, R, F = _prf(totals["tp"], totals["fp"], totals["fn"])
    res["micro"] = {**totals, "precision": P, "recall": R, "f1": F,
                    "omission_rate": round(1 - R, 4)}
    return res


def print_table(res):
    print(f"{'Nhóm fact':<16}{'GT':>6}{'Pred':>6}{'TP':>6}{'FP':>6}{'FN':>6}{'P':>8}{'R':>8}{'F1':>8}")
    for cat, s in res["by_category"].items():
        print(f"{cat:<16}{s['gt']:>6}{s['pred']:>6}{s['tp']:>6}{s['fp']:>6}{s['fn']:>6}"
              f"{s['precision']:>8.3f}{s['recall']:>8.3f}{s['f1']:>8.3f}")
    m = res["micro"]
    print(f"{'MICRO':<16}{'':>6}{'':>6}{m['tp']:>6}{m['fp']:>6}{m['fn']:>6}{m['precision']:>8.3f}{m['recall']:>8.3f}{m['f1']:>8.3f}")
    if res["wrong_value"]:
        print(f"\nRàng buộc đúng vị trí nhưng sai giá trị: {len(res['wrong_value'])}")
        for w in res["wrong_value"][:15]:
            print(f"  {w['key']}: GT={w['gt']!r} | pred={w['pred']!r}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pred", required=True, help="đặc tả cần chấm (YAML/JSON)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--gt", help="đặc tả ground truth")
    g.add_argument("--api", help="id API trong apis/ (dùng ground truth của bộ dữ liệu)")
    ap.add_argument("--gt-kind", choices=["doc", "behavior"], default="doc")
    ap.add_argument("--no-type", action="store_true", help="bỏ các ràng buộc 'type' khỏi nhóm constraint")
    ap.add_argument("--report", help="ghi kết quả chi tiết ra JSON")
    a = ap.parse_args()
    if a.api:
        name = "openapi.yaml" if a.gt_kind == "doc" else "behavior_openapi.yaml"
        gt_path = ROOT / "apis" / a.api / "ground_truth" / name
    else:
        gt_path = Path(a.gt)
    gt_facts = extract(load_spec(gt_path))
    pred_facts = extract(load_spec(a.pred))
    kws = None
    if a.no_type:
        kws = {f["keyword"] for f in gt_facts + pred_facts if f["category"] == "constraint"} - {"type"}
    res = compare(gt_facts, pred_facts, kws)
    res["gt_path"], res["pred_path"] = str(gt_path), a.pred
    print_table(res)
    if a.report:
        Path(a.report).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\nĐã ghi báo cáo chi tiết: {a.report}")


if __name__ == "__main__":
    main()
