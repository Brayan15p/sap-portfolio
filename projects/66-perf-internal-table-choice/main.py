import bisect
def read_cost(kind, n, lookups):
    data = list(range(n)); cost = 0
    for k in lookups:
        if kind == "STANDARD": cost += data.index(k) + 1
        elif kind == "SORTED":
            lo, hi, c = 0, n, 0
            while lo < hi:
                c += 1; mid = (lo + hi) // 2
                if data[mid] < k: lo = mid + 1
                else: hi = mid
            cost += c
        elif kind == "HASHED": cost += 1
    return cost
def recommend(unique_key: bool, needs_order: bool, mostly_key_reads: bool):
    if mostly_key_reads and unique_key and not needs_order: return "HASHED"
    if mostly_key_reads or needs_order: return "SORTED"
    return "STANDARD"
