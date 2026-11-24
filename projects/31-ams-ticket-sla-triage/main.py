from datetime import datetime, timedelta

MATRIX = {("HIGH", "HIGH"): "P1", ("HIGH", "MEDIUM"): "P2", ("MEDIUM", "HIGH"): "P2",
          ("MEDIUM", "MEDIUM"): "P3", ("LOW", "HIGH"): "P3"}
SLA_HOURS = {"P1": 4, "P2": 8, "P3": 24, "P4": 40}

def priority(impact, urgency): return MATRIX.get((impact, urgency), "P4")

def business_hours_between(start: datetime, end: datetime, pauses=()):
    t, secs = start, 0
    while t < end:
        nxt = min(end, t + timedelta(minutes=15))
        in_hours = t.weekday() < 5 and 8 <= t.hour < 18
        paused = any(p0 <= t < p1 for p0, p1 in pauses)
        if in_hours and not paused: secs += (nxt - t).total_seconds()
        t = nxt
    return secs / 3600

def sla_state(ticket, now: datetime, warn_ratio=0.8):
    p = priority(ticket["impact"], ticket["urgency"])
    used = business_hours_between(ticket["opened"], now, ticket.get("pauses", ()))
    limit = SLA_HOURS[p]
    state = "BREACHED" if used > limit else "ESCALATE" if used >= limit * warn_ratio else "OK"
    return {"priority": p, "used_h": round(used, 2), "limit_h": limit, "state": state}
