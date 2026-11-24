def schedule(orders, capacity, today=0):
    """orders: [{id, due, ops:[(wc, hours)]}] in priority order. capacity: {wc: hours/day}. Days are integers."""
    load = {}   # (wc, day) -> hours used
    plan, late = {}, []
    for o in orders:
        day, steps = o["due"], []
        for wc, hours in reversed(o["ops"]):
            remaining = hours
            while remaining > 0:
                day -= 0 if load.get((wc, day), 0) < capacity[wc] else 1
                free = capacity[wc] - load.get((wc, day), 0)
                if free <= 0: day -= 1; continue
                take = min(free, remaining)
                load[(wc, day)] = load.get((wc, day), 0) + take; remaining -= take
                steps.append((wc, day, take))
                if remaining > 0: day -= 1
            day -= 1
        start = min(s[1] for s in steps)
        plan[o["id"]] = sorted(steps, key=lambda s: s[1])
        if start < today:
            late.append({"order": o["id"], "start": start, "bottleneck": max(o["ops"], key=lambda op: op[1] / capacity[op[0]])[0]})
    return plan, late, load
