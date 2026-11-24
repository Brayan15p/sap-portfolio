GATES = [  # (key, weight, threshold, hard)
    ("data_ready_pct", 0.20, 98, True),
    ("open_critical_defects", 0.20, 0, True),
    ("integration_tests_pass_pct", 0.15, 95, True),
    ("cutover_rehearsal_fits_window", 0.15, True, True),
    ("unmitigated_high_sod", 0.10, 0, False),
    ("users_trained_pct", 0.10, 90, False),
    ("hypercare_staffed", 0.10, True, False),
]
def passes(key, value, threshold):
    if isinstance(threshold, bool): return value is threshold
    return value <= threshold if key in ("open_critical_defects", "unmitigated_high_sod") else value >= threshold
def readiness(metrics):
    score, failed_hard, failed_soft = 0.0, [], []
    for key, w, thr, hard in GATES:
        ok = passes(key, metrics[key], thr)
        score += w * (1 if ok else 0)
        if not ok: (failed_hard if hard else failed_soft).append(key)
    decision = "NO-GO" if failed_hard else "GO" if not failed_soft else "GO WITH RISKS"
    return {"score": round(score * 100), "decision": decision, "failed_hard": failed_hard, "failed_soft": failed_soft}
