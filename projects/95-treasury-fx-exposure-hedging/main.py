def exposure(items, policy=((0, 90, 0.75), (91, 180, 0.5))):
    buckets = {}
    for i in items:
        sign = -1 if i["kind"] == "AP" else 1
        b = next((f"{lo}-{hi}" for lo, hi, _ in policy if lo <= i["days"] <= hi), None)
        if b: buckets.setdefault((i["ccy"], b), 0); buckets[(i["ccy"], b)] += sign * i["amount"]
    ratio = {f"{lo}-{hi}": r for lo, hi, r in policy}
    proposals = []
    for (ccy, b), net in buckets.items():
        if net < 0: proposals.append({"ccy": ccy, "bucket": b, "net_exposure": net, "buy_forward": round(-net * ratio[b], 2)})
    return buckets, proposals
