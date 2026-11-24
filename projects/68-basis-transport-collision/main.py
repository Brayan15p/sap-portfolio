def collisions(transports):
    by_obj = {}
    for t in transports:
        for o in t["objects"]: by_obj.setdefault(o, []).append(t)
    out = []
    for o, ts in by_obj.items():
        if len(ts) < 2: continue
        ts_sorted = sorted(ts, key=lambda t: t["released"])
        out.append({"object": o, "transports": [t["id"] for t in ts_sorted]})
    return out
def downgrade_risk(import_queue, transports):
    rel = {t["id"]: t["released"] for t in transports}; objs = {t["id"]: set(t["objects"]) for t in transports}
    risks = []
    for i, a in enumerate(import_queue):
        for b in import_queue[i + 1:]:
            common = objs[a] & objs[b]
            if common and rel[b] < rel[a]: risks.append({"older": b, "after": a, "objects": sorted(common)})
    return risks
