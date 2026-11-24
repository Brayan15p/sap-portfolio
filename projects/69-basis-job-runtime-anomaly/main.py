from statistics import median
def anomalies(history, latest, k=5.0):
    out = []
    for job, runs in history.items():
        med = median(runs); mad = median(abs(r - med) for r in runs) or 1
        score = (latest[job] - med) / (1.4826 * mad)
        if score > k: out.append({"job": job, "baseline_min": med, "latest_min": latest[job], "score": round(score, 1)})
    return sorted(out, key=lambda x: -x["score"])
