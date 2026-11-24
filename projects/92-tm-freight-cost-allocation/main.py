def chargeable(kg, m3, factor=250): return max(kg, m3 * factor)
def allocate(freight_cost, deliveries):
    w = {d["id"]: chargeable(d["kg"], d["m3"]) for d in deliveries}; total = sum(w.values())
    shares = {k: round(freight_cost * v / total) for k, v in w.items()}
    shares[max(w, key=w.get)] += freight_cost - sum(shares.values())
    return shares
