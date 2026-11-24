from decimal import Decimal, ROUND_HALF_UP

def q(x): return Decimal(x).quantize(Decimal("0.01"), ROUND_HALF_UP)

def cost(material, bom, prices, routing, rates, overhead_pct=Decimal("8"), _path=()):
    if material in _path: raise ValueError(f"Recursive BOM: {' > '.join(_path + (material,))}")
    if material in prices:
        return {"material": q(prices[material]), "labor": Decimal(0), "overhead": Decimal(0), "total": q(prices[material])}
    mat = lab = Decimal(0)
    for comp, qty, scrap_pct in bom[material]["components"]:
        c = cost(comp, bom, prices, routing, rates, overhead_pct, _path + (material,))
        factor = Decimal(qty) * (1 + Decimal(scrap_pct) / 100) / bom[material]["base_qty"]
        mat += c["material"] * factor + c["overhead"] * factor; lab += c["labor"] * factor
    for wc, minutes in routing.get(material, []):
        lab += Decimal(minutes) / 60 * Decimal(rates[wc]) / bom[material]["base_qty"]
    ovh = mat * overhead_pct / 100
    return {"material": q(mat), "labor": q(lab), "overhead": q(ovh), "total": q(mat + lab + ovh)}
