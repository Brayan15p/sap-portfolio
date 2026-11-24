def apr(discount_pct, days_early):
    return round((discount_pct / (100 - discount_pct)) * (365 / days_early) * 100, 2)
def sliding_discount(days_early, max_pct=2.0, full_days=30):
    return round(max_pct * min(days_early, full_days) / full_days, 3)
def select(invoices, cash, hurdle_apr):
    cands = []
    for i in invoices:
        d = sliding_discount(i["days_early"]); a = apr(d, i["days_early"])
        if a >= hurdle_apr: cands.append({**i, "discount_pct": d, "apr": a, "pay": round(i["amount"] * (1 - d / 100), 2)})
    cands.sort(key=lambda c: -c["apr"]); chosen, used = [], 0
    for c in cands:
        if used + c["pay"] <= cash: chosen.append(c); used += c["pay"]
    return chosen, round(sum(c["amount"] - c["pay"] for c in chosen), 2)
