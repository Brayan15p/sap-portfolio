def compare(quotes, conversions):
    """quotes: [{vendor, uom, price, freight}], conversions: uom -> base units"""
    ranked = []
    for q in quotes:
        if q["uom"] not in conversions:
            raise ValueError(f"No conversion for UoM {q['uom']}")
        per_unit = (q["price"] + q.get("freight", 0)) / conversions[q["uom"]]
        ranked.append({**q, "per_base_unit": round(per_unit, 4)})
    return sorted(ranked, key=lambda r: r["per_base_unit"])
