FACTORS_SPEND = {"Transport": 0.00045, "Packaging": 0.00060, "IT": 0.00020, "Food": 0.00080}   # kg CO2e per COP (illustrative)
FACTORS_ACTIVITY = {"diesel_l": 2.68, "electricity_kwh": 0.126}                                  # kg CO2e per unit (illustrative)
def footprint(lines):
    by_sup, total = {}, 0.0
    for l in lines:
        kg = l["qty"] * FACTORS_ACTIVITY[l["activity"]] if l.get("activity") else l["amount"] * FACTORS_SPEND[l["category"]]
        by_sup[l["supplier"]] = by_sup.get(l["supplier"], 0) + kg; total += kg
    ranked = sorted(by_sup.items(), key=lambda kv: -kv[1]); cum, hot = 0, []
    for s, kg in ranked:
        if cum / total >= 0.8: break
        hot.append(s); cum += kg
    return {"total_t": round(total / 1000, 2), "by_supplier_t": {s: round(k / 1000, 2) for s, k in ranked}, "hotspots_80pct": hot}
