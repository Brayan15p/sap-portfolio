import re
from collections import defaultdict
def analyze(trace_lines):
    stats = defaultdict(lambda: {"exec": 0, "ms": 0.0, "rows": 0})
    for l in trace_lines:
        m = re.match(r"\s*(?P<ms>[\d.]+)ms\s+(?P<rows>\d+)\s+(?P<sql>.+)", l)
        if not m: continue
        sql = re.sub(r"'[^']*'|\b\d+\b", "?", m["sql"].strip().upper())
        s = stats[sql]; s["exec"] += 1; s["ms"] += float(m["ms"]); s["rows"] += int(m["rows"])
    findings = []
    for sql, s in sorted(stats.items(), key=lambda kv: -kv[1]["ms"]):
        if s["exec"] >= 10: findings.append(("IDENTICAL_REPEATED", sql, s, "Read once before the loop (FOR ALL ENTRIES / JOIN)"))
        if "WHERE" not in sql: findings.append(("NO_WHERE", sql, s, "Add WHERE on key/index fields"))
    return findings, dict(stats)
