from main import credits
T = [{"id": f"P1-{i}", "priority": "P1", "sla_h": 4, "resolved_h": 3} for i in range(18)] + \
    [{"id": "P1-x", "priority": "P1", "sla_h": 4, "resolved_h": 9}, {"id": "P1-y", "priority": "P1", "sla_h": 4, "resolved_h": 6}] + \
    [{"id": "P2-1", "priority": "P2", "sla_h": 8, "resolved_h": 5}]
def test_credit_and_breaches():
    r, total = credits(T, 100_000_000)
    assert r["P1"]["compliance"] == 0.9 and r["P1"]["breaches"] == ["P1-x", "P1-y"] and total == 5_000_000
