def variance(plan, actuals, reallocations=()):
    act = {}
    for a in actuals:
        k = (a["cc"], a["period"]); act[k] = act.get(k, 0) + a["amount"]
    for r in reallocations:
        act[(r["from"], r["period"])] = act.get((r["from"], r["period"]), 0) - r["amount"]
        act[(r["to"], r["period"])] = act.get((r["to"], r["period"]), 0) + r["amount"]
    out = {}
    for k in set(plan) | set(act):
        p, a = plan.get(k, 0), act.get(k, 0)
        out[k] = {"plan": p, "actual": a, "var": a - p, "pct": round((a - p) / p * 100, 1) if p else None}
    return out
