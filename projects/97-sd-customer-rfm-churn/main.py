from datetime import date
def quintile(values, v, reverse=False):
    s = sorted(values); rank = sum(1 for x in s if x <= v) / len(s)
    q = min(5, max(1, int(rank * 5 + 0.999)))
    return 6 - q if reverse else q
def rfm(orders, today: date):
    agg = {}
    for o in orders:
        a = agg.setdefault(o["customer"], {"last": o["date"], "f": 0, "m": 0})
        a["last"] = max(a["last"], o["date"]); a["f"] += 1; a["m"] += o["amount"]
    R = {c: (today - a["last"]).days for c, a in agg.items()}
    out = {}
    for c, a in agg.items():
        r = quintile(list(R.values()), R[c], reverse=True); f = quintile([x["f"] for x in agg.values()], a["f"]); m = quintile([x["m"] for x in agg.values()], a["m"])
        seg = ("NEW" if a["f"] == 1 and r >= 4 else "CHAMPION" if r >= 4 and f >= 4
               else "AT_RISK" if r <= 2 and f >= 3 else "REGULAR")
        out[c] = {"R": r, "F": f, "M": m, "segment": seg}
    return out
