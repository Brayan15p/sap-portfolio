COUNTRY = {"CO": 0.3, "MX": 0.3, "US": 0.1, "DE": 0.1, "CN": 0.5, "VE": 0.9}
def score(suppliers, sources):
    out = {}
    for s, d in suppliers.items():
        single = [m for m, sup in sources.items() if sup == [s]]
        r = 0.3 * COUNTRY.get(d["country"], 0.6) + 0.3 * min(1, len(single) / 3) + 0.2 * (1 - d["on_time"]) + 0.2 * (1 if d["financial_alert"] else 0)
        out[s] = {"risk": round(r, 3), "single_sourced": single, "level": "HIGH" if r >= 0.5 else "MEDIUM" if r >= 0.3 else "LOW"}
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["risk"]))
