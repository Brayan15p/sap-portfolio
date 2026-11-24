# Illustrative thresholds; real values per state change and must be maintained.
THRESHOLDS = {"CA": {"sales": 500_000, "tx": None, "rule": "sales"},
              "TX": {"sales": 500_000, "tx": None, "rule": "sales"},
              "NY": {"sales": 500_000, "tx": 100, "rule": "and"},
              "GA": {"sales": 100_000, "tx": 200, "rule": "or"}}

def nexus(orders, warn_ratio=0.8):
    agg = {}
    for o in orders:
        a = agg.setdefault(o["state"], {"sales": 0, "tx": 0}); a["sales"] += o["amount"]; a["tx"] += 1
    status = {}
    for st, a in agg.items():
        t = THRESHOLDS.get(st)
        if not t: status[st] = "NO_RULE"; continue
        s_hit = a["sales"] >= t["sales"]; tx_hit = t["tx"] is not None and a["tx"] >= t["tx"]
        hit = s_hit if t["rule"] == "sales" else (s_hit and tx_hit) if t["rule"] == "and" else (s_hit or tx_hit)
        near = a["sales"] >= t["sales"] * warn_ratio or (t["tx"] and a["tx"] >= t["tx"] * warn_ratio)
        status[st] = "NEXUS" if hit else "WARNING" if near else "OK"
    return status
