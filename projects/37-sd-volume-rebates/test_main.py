from main import accruals

def test_retroactive_catch_up_when_tier_jumps():
    rows, total = accruals([300_000_000, 300_000_000, 500_000_000])
    assert rows[0]["accrual"] == 0
    assert rows[1]["rate"] == 2.0 and rows[1]["accrual"] == 12_000_000 and rows[1]["catch_up"]
    assert rows[2]["rate"] == 3.0 and total == 33_000_000

def test_settlement_equals_sum_of_accruals():
    rows, total = accruals([100_000_000] * 12)
    assert sum(r["accrual"] for r in rows) == total == 36_000_000
