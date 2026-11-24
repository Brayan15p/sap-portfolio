from main import readiness
GOOD = {"data_ready_pct": 99.2, "open_critical_defects": 0, "integration_tests_pass_pct": 97, "cutover_rehearsal_fits_window": True,
        "unmitigated_high_sod": 0, "users_trained_pct": 93, "hypercare_staffed": True}
def test_go():
    assert readiness(GOOD) == {"score": 100, "decision": "GO", "failed_hard": [], "failed_soft": []}
def test_hard_gate_blocks_even_with_high_score():
    r = readiness({**GOOD, "open_critical_defects": 3})
    assert r["decision"] == "NO-GO" and r["score"] == 80
def test_soft_gates():
    assert readiness({**GOOD, "users_trained_pct": 60})["decision"] == "GO WITH RISKS"
