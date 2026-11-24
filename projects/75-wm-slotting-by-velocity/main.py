def slot(skus, bins):
    """skus: {sku: (picks, volume_m3)}, bins: {bin: (distance_m, capacity_m3)}"""
    order = sorted(skus, key=lambda s: -skus[s][0] / skus[s][1])
    free = sorted(bins, key=lambda b: bins[b][0]); assign = {}
    for s in order:
        b = next((b for b in free if bins[b][1] >= skus[s][1]), None)
        if b is None: raise ValueError(f"No bin fits {s}")
        assign[s] = b; free.remove(b)
    return assign
def walking(assign, skus, bins):
    return sum(skus[s][0] * bins[b][0] * 2 for s, b in assign.items())
