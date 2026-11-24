from decimal import Decimal
from main import lease_schedule

def test_initial_recognition_and_full_amortization():
    s = lease_schedule(10_000_000, 60, 12)
    assert Decimal("449000000") < s["initial_liability"] < Decimal("450000000")
    assert s["rows"][-1]["liability"] == 0
    total_interest = sum(r["interest"] for r in s["rows"])
    assert abs(total_interest - (600_000_000 - s["initial_liability"])) < 100

def test_interest_decreases_over_time_and_idc_in_rou():
    s = lease_schedule(1000, 12, 10, initial_direct_costs=500)
    assert s["rows"][0]["interest"] > s["rows"][-1]["interest"]
    assert s["initial_rou"] == s["initial_liability"] + 500
