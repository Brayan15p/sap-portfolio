import re
from collections import defaultdict

HINTS = {
    "TSV_TNEW_PAGE_ALLOC_FAILED": "Memory: check internal table growth and SELECT without WHERE/PACKAGE SIZE",
    "CX_SY_ZERODIVIDE": "Guard divisions; check master data with zero quantities or prices",
    "DBSQL_DUPLICATE_KEY_ERROR": "Duplicate insert: check number ranges or missing existence check",
    "TIME_OUT": "Long runtime: review nested loops, missing indexes, run in background",
    "CX_SY_ITAB_LINE_NOT_FOUND": "READ TABLE / table expression without existence check",
}

LINE = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\S+) (?P<user>\S+) (?P<exc>[A-Z_]+) (?P<prog>\S+) (?P<incl>\S+) (?P<line>\d+)")

def analyze(export_text, top=3):
    groups = defaultdict(lambda: {"count": 0, "users": set()})
    bad = 0
    for raw in export_text.strip().splitlines():
        m = LINE.match(raw.strip())
        if not m: bad += 1; continue
        k = (m["exc"], m["prog"], m["incl"], int(m["line"]))
        groups[k]["count"] += 1; groups[k]["users"].add(m["user"])
    ranked = sorted(groups.items(), key=lambda kv: (-kv[1]["count"], -len(kv[1]["users"])))
    return {"unparsed": bad, "top": [{"exception": k[0], "program": k[1], "include": k[2], "line": k[3],
                                      "count": v["count"], "users": len(v["users"]), "hint": HINTS.get(k[0], "Open ST22 and analyze source position")}
                                     for k, v in ranked[:top]]}
