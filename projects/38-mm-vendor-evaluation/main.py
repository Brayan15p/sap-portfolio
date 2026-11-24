def evaluate(deliveries, prices, weights=None, threshold=70):
    w = weights or {"price": 0.4, "on_time": 0.35, "quality": 0.25}
    assert abs(sum(w.values()) - 1) < 1e-9, "weights must sum to 1"
    best = min(prices.values())
    out = {}
    for v in prices:
        d = [x for x in deliveries if x["vendor"] == v]
        on_time = 100 * sum(1 for x in d if x["days_late"] <= 0) / len(d) if d else 0
        quality = 100 * (1 - sum(x["rejected"] for x in d) / sum(x["qty"] for x in d)) if d else 0
        price = 100 * best / prices[v]
        score = round(w["price"] * price + w["on_time"] * on_time + w["quality"] * quality, 1)
        out[v] = {"price": round(price, 1), "on_time": round(on_time, 1), "quality": round(quality, 1), "score": score, "review": score < threshold}
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["score"]))
