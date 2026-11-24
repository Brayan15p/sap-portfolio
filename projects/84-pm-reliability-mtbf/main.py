import math
def reliability(events, hours_window, next_hours, criticality):
    out = {}
    for eq, ev in events.items():
        failures = len(ev); downtime = sum(e["repair_h"] for e in ev)
        uptime = hours_window - downtime
        mtbf = uptime / failures if failures else float("inf"); mttr = downtime / failures if failures else 0
        p_fail = 1 - math.exp(-next_hours / mtbf) if failures else 0.0
        out[eq] = {"mtbf_h": round(mtbf, 1), "mttr_h": round(mttr, 1), "availability": round(uptime / hours_window, 4),
                   "p_fail_next": round(p_fail, 3), "risk": round(p_fail * criticality[eq], 3)}
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["risk"]))
