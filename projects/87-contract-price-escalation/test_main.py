from decimal import Decimal
from main import adjust, back_billing
def test_formula_with_cap_and_back_billing():
    h = adjust(10_000_000, [{"labor": 9.5, "materials": 4.0}, {"labor": 12, "materials": 10}], weights={"labor": 0.6, "materials": 0.4}, cap_pct=10)
    assert h[0][2] == Decimal("10730000") and h[1][1] == 10.0
    assert back_billing(10_000_000, 10_730_000, 3, 1) == Decimal("2190000")
