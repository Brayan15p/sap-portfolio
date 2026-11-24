def cpm(tasks, window_hours):
    """tasks: {id: (duration_h, [deps])}"""
    order, seen = [], set()
    def visit(t, stack=()):
        if t in stack: raise ValueError(f"cycle at {t}")
        if t in seen: return
        for d in tasks[t][1]: visit(d, stack + (t,))
        seen.add(t); order.append(t)
    for t in tasks: visit(t)
    es = {}; ef = {}
    for t in order:
        es[t] = max((ef[d] for d in tasks[t][1]), default=0); ef[t] = es[t] + tasks[t][0]
    end = max(ef.values()); lf = {t: end for t in tasks}; ls = {}
    for t in reversed(order):
        succ = [s for s in tasks if t in tasks[s][1]]
        lf[t] = min((ls[s] for s in succ), default=end); ls[t] = lf[t] - tasks[t][0]
    slack = {t: ls[t] - es[t] for t in tasks}
    critical = [t for t in order if slack[t] == 0]
    return {"duration": end, "critical_path": critical, "slack": slack, "fits_window": end <= window_hours}
