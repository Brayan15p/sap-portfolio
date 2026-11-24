def holt(series, alpha, beta, horizon):
    level, trend = series[0], series[1] - series[0]; fitted = [series[0]]
    for y in series[1:]:
        fitted.append(level + trend)
        prev = level; level = alpha * y + (1 - alpha) * (level + trend); trend = beta * (level - prev) + (1 - beta) * trend
    return fitted, [level + (h + 1) * trend for h in range(horizon)]
def mape(actual, fitted):
    pairs = [(a, f) for a, f in zip(actual[1:], fitted[1:]) if a]
    return 100 * sum(abs(a - f) / a for a, f in pairs) / len(pairs)
def best_forecast(series, horizon=3):
    grid = [i / 10 for i in range(1, 10)]
    a, b = min(((a, b) for a in grid for b in grid), key=lambda ab: mape(series, holt(series, *ab, 0)[0]))
    fitted, fc = holt(series, a, b, horizon)
    return {"alpha": a, "beta": b, "mape": round(mape(series, fitted), 2), "forecast": [round(x, 1) for x in fc]}
