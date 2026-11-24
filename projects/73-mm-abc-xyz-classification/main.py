from statistics import mean, pstdev
def classify(items):
    vals = sorted(((k, sum(v["demand"]) * v["price"]) for k, v in items.items()), key=lambda kv: -kv[1])
    total = sum(v for _, v in vals); cum = 0; out = {}
    for k, v in vals:
        cum += v; share = cum / total
        abc = "A" if share <= 0.80 or cum == v else "B" if share <= 0.95 else "C"
        d = items[k]["demand"]; cv = pstdev(d) / mean(d) if mean(d) else 99
        xyz = "X" if cv <= 0.25 else "Y" if cv <= 0.5 else "Z"
        out[k] = abc + xyz
    return out
