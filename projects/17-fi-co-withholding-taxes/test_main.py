from decimal import Decimal
from main import withholdings

UVT = 50000  # illustrative

def test_service_above_minimum_full_breakdown():
    w = withholdings(1_000_000, 190_000, "SERVICIOS", UVT, "9.66")
    assert w["retefuente"] == 40_000 and w["reteiva"] == 28_500 and w["reteica"] == 9_660
    assert w["net_payable"] == 1_190_000 - 40_000 - 28_500 - 9_660

def test_purchase_below_minimum_base_has_no_retefuente():
    assert withholdings(1_000_000, 190_000, "COMPRAS", UVT, "0")["retefuente"] == 0

def test_vendor_not_responsible_no_reteiva_and_entry_balances():
    w = withholdings(500_000, 0, "HONORARIOS", UVT, "0", vendor_is_iva_responsible=False)
    assert w["reteiva"] == 0 and w["retefuente"] == 55_000
