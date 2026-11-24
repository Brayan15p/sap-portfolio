TARGETS = {"P1": (0.95, 0.05), "P2": (0.90, 0.03), "P3": (0.85, 0.01)}   # (target compliance, credit % of fee if missed)
def credits(tickets, monthly_fee, cap_pct=0.15):
    out, total = {}, 0.0
    for p, (target, credit) in TARGETS.items():
        t = [x for x in tickets if x["priority"] == p]
        if not t: continue
        met = sum(1 for x in t if x["resolved_h"] <= x["sla_h"]); comp = met / len(t)
        c = monthly_fee * credit if comp < target else 0; total += c
        out[p] = {"compliance": round(comp, 3), "credit": c, "breaches": [x["id"] for x in t if x["resolved_h"] > x["sla_h"]]}
    return out, min(total, monthly_fee * cap_pct)
