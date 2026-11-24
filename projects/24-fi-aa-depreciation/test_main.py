from decimal import Decimal
from main import schedule

def test_starts_next_month_and_never_below_salvage():
    s = schedule(1_200_000, 120_000, 12, cap_month=1, months=20)
    assert s[0][1] == 0 and s[1][1] == Decimal("90000.00")
    assert s[-1][2] == Decimal("120000.00")

def test_partial_retirement_halves_future_depreciation():
    s = schedule(1_200_000, 0, 12, 1, 6, retirements={4: 0.5})
    assert s[2][1] == Decimal("100000.00") and s[3][1] == Decimal("50000.00")
