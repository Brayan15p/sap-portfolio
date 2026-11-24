import heapq
def schedule(jobs, slots, start=0, deadline=None):
    """jobs: {id: (minutes, [deps])}"""
    indeg = {j: len(d) for j, (_, d) in jobs.items()}; ready = [j for j, n in indeg.items() if n == 0]
    free = [start] * slots; heapq.heapify(free); finish, plan = {}, []
    while ready:
        ready.sort(key=lambda j: -jobs[j][0])
        j = ready.pop(0)
        slot_free = heapq.heappop(free)
        st = max(slot_free, max((finish[d] for d in jobs[j][1]), default=start))
        finish[j] = st + jobs[j][0]; heapq.heappush(free, finish[j]); plan.append((j, st, finish[j]))
        for k, (_, d) in jobs.items():
            if j in d:
                indeg[k] -= 1
                if indeg[k] == 0: ready.append(k)
    if len(finish) != len(jobs): raise ValueError("cyclic dependency")
    late = [j for j, f in finish.items() if deadline is not None and f > deadline]
    return plan, max(finish.values()), late
