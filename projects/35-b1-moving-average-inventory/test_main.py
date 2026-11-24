import pytest
from decimal import Decimal
from main import Item

def test_average_moves_and_issue_cost():
    i = Item(); i.receive(100, 1000, "GR1"); i.receive(100, 1200, "GR2")
    assert i.avg == Decimal("1100") and i.issue(50, "DN1") == Decimal("55000")

def test_return_at_receipt_price_changes_average():
    i = Item(); i.receive(100, 1000, "GR1"); i.receive(100, 1200, "GR2"); i.return_to_vendor(100, 1200, "RT1")
    assert i.avg == Decimal("1000")

def test_negative_stock_refused():
    i = Item(); i.receive(10, 1, "GR1")
    with pytest.raises(ValueError, match="negative stock"): i.issue(11, "DN1")
