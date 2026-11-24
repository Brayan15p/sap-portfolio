def build_loads(deliveries, max_kg, max_m3):
    loads = []
    for d in sorted(deliveries, key=lambda d: -max(d["kg"] / max_kg, d["m3"] / max_m3)):
        if d["kg"] > max_kg or d["m3"] > max_m3: raise ValueError(f"{d['id']} does not fit any truck")
        for L in loads:
            if L["kg"] + d["kg"] <= max_kg and L["m3"] + d["m3"] <= max_m3:
                L["items"].append(d["id"]); L["kg"] += d["kg"]; L["m3"] += d["m3"]; break
        else:
            loads.append({"items": [d["id"]], "kg": d["kg"], "m3": d["m3"]})
    for L in loads: L["util"] = round(max(L["kg"] / max_kg, L["m3"] / max_m3), 2)
    return loads
