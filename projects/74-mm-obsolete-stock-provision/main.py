from datetime import date
POLICY = [(365, 1.00, "OBSOLETE"), (180, 0.50, "SLOW_180"), (90, 0.20, "SLOW_90")]
def provision(stock, today: date):
    rows, total = [], 0
    for s in stock:
        idle = (today - s["last_issue"]).days
        expired = s.get("expiry") and s["expiry"] < today
        pct, bucket = (1.0, "EXPIRED") if expired else next(((p, b) for d, p, b in POLICY if idle >= d), (0.0, "ACTIVE"))
        amount = round(s["qty"] * s["unit_cost"] * pct, 2); total += amount
        rows.append({"material": s["material"], "bucket": bucket, "provision": amount})
    return rows, round(total, 2), [("Inventory write-down expense", total, 0), ("Inventory provision", 0, total)]
