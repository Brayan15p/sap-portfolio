import math
def replenish(stores, promo_uplift, days_cover):
    out = {}
    for s, d in stores.items():
        daily = d["avg_daily"] * (1 + promo_uplift.get(s, 0))
        need = daily * days_cover + d["safety"] - d["on_hand"] - d["in_transit"]
        if need <= 0: out[s] = 0; continue
        qty = math.ceil(need / d["case_pack"]) * d["case_pack"]
        cap = d["shelf_capacity"] - d["on_hand"] - d["in_transit"]
        out[s] = max(0, min(qty, (cap // d["case_pack"]) * d["case_pack"]))
    return out
