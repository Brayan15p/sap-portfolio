from main import variance

PLAN = {("CC1", "2026-11"): 1000, ("CC2", "2026-11"): 500}
ACT = [{"cc": "CC1", "period": "2026-11", "amount": 1200}]

def test_variance_pct():
    assert variance(PLAN, ACT)[("CC1", "2026-11")]["pct"] == 20.0

def test_reallocation_preserves_total():
    r = variance(PLAN, ACT, [{"from": "CC1", "to": "CC2", "period": "2026-11", "amount": 200}])
    assert r[("CC1", "2026-11")]["actual"] == 1000 and r[("CC2", "2026-11")]["actual"] == 200
    assert sum(v["actual"] for v in r.values()) == 1200
