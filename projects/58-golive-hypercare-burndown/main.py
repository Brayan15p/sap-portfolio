def hypercare(days):
    backlog, rows, growth_streak, alert_day = 0, [], 0, None
    for i, d in enumerate(days, 1):
        prev = backlog; backlog += d["opened"] - d["closed"]
        growth_streak = growth_streak + 1 if backlog > prev else 0
        if growth_streak >= 3 and alert_day is None: alert_day = i
        rows.append({"day": i, "backlog": backlog})
    last3 = days[-3:]
    net = sum(d["closed"] - d["opened"] for d in last3) / len(last3)
    eta = round(backlog / net, 1) if net > 0 else None
    return {"rows": rows, "alert_day": alert_day, "days_to_clear": eta}
