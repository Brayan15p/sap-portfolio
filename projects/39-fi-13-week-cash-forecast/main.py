from datetime import date, timedelta

def forecast(opening, start: date, receivables, payables, fixed_weekly, behavior, minimum):
    weeks = [{"week": i + 1, "start": start + timedelta(weeks=i), "in": 0, "out": fixed_weekly} for i in range(13)]
    def idx(d): return (d - start).days // 7
    for r in receivables:
        expected = r["due"] + timedelta(days=behavior.get(r["customer"], 0))
        i = max(0, idx(expected))
        if i < 13: weeks[i]["in"] += r["amount"]
    for p in payables:
        i = max(0, idx(p["due"]))
        if i < 13: weeks[i]["out"] += p["amount"]
    bal, alert = opening, None
    for w in weeks:
        bal += w["in"] - w["out"]; w["closing"] = bal
        if alert is None and bal < minimum: alert = w["week"]
    return weeks, alert
