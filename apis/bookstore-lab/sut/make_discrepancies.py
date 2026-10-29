"""Sinh ground_truth/discrepancies.json từ discrepancies.src.yaml + so sánh fact doc-GT với behavior-GT."""
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GT = HERE.parent / "ground_truth"
sys.path.insert(0, str(HERE.parent.parent.parent / "tools"))
from extract_facts import extract  # noqa: E402
from oas_utils import load_spec  # noqa: E402

src = yaml.safe_load((GT / "discrepancies.src.yaml").read_text(encoding="utf-8"))
doc = {f["key"]: f for f in extract(load_spec(GT / "openapi.yaml"))}
beh = {f["key"]: f for f in extract(load_spec(GT / "behavior_openapi.yaml"))}
diff = {
    "only_in_doc": sorted(k for k in doc if k not in beh),
    "only_in_behavior": sorted(k for k in beh if k not in doc),
    "value_changed": sorted(
        [{"key": k, "doc": doc[k].get("value"), "behavior": beh[k].get("value")}
         for k in doc if k in beh and doc[k].get("value") != beh[k].get("value")], key=lambda x: x["key"]),
}
out = {
    "api": "bookstore-lab",
    "description": "Sai lệch tài liệu – cài đặt được cài cắm có chủ đích. 'discrepancies' là danh sách mức người đọc "
                   "(mỗi mục kèm probe tái hiện); 'fact_level_diff' là khác biệt ở mức atomic fact giữa doc-GT và behavior-GT.",
    "discrepancies": src["discrepancies"],
    "controls": src["controls"],
    "non_expressible": src.get("non_expressible", []),
    "fact_level_diff": diff,
    "summary": {"n_discrepancies": len(src["discrepancies"]),
                "by_code": {c: sum(1 for d in src["discrepancies"] if d["code"] == c)
                            for c in sorted({d["code"] for d in src["discrepancies"]})},
                "n_controls": len(src["controls"]),
                "fact_diff_counts": {k: len(v) for k, v in diff.items()}},
}
(GT / "discrepancies.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(out["summary"], ensure_ascii=False, indent=1))
