from decimal import Decimal, ROUND_HALF_UP

def q(x): return Decimal(x).quantize(Decimal("1"), ROUND_HALF_UP)

def allocate(total, weights):
    total = Decimal(total); weights = {k: Decimal(str(w)) for k, w in weights.items()}; tw = sum(weights.values())
    shares = {k: q(total * Decimal(w) / tw) for k, w in weights.items()}
    shares[max(weights, key=weights.get)] += q(total) - sum(shares.values())
    return shares

def landed_costs(items, freight, insurance, handling, trm):
    """items: {code: {qty, fob_usd, weight_kg, duty_pct}}"""
    fob = {k: q(Decimal(v["fob_usd"]) * v["qty"] * Decimal(trm)) for k, v in items.items()}
    fr = allocate(freight, fob); ins = allocate(insurance, fob)
    hd = allocate(handling, {k: v["weight_kg"] * v["qty"] for k, v in items.items()})
    out = {}
    for k, v in items.items():
        cif = fob[k] + fr[k] + ins[k]
        duty = q(cif * Decimal(v["duty_pct"]) / 100)
        total = cif + duty + hd[k]
        out[k] = {"fob": fob[k], "freight": fr[k], "insurance": ins[k], "duty": duty, "handling": hd[k],
                  "total": total, "unit_cost": q(total / v["qty"]), "uplift_pct": round(float((total - fob[k]) / fob[k] * 100), 1)}
    return out
