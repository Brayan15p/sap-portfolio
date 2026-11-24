import pytest
from main import SalesOrder

def make():
    o = SalesOrder(1); o.add(0, "A1001", 20); o.add(1, "A2002", 5); return o

def test_partial_shows_pending():
    o = make(); o.deliver(0, 12)
    assert o.lines[0].open_qty == 8 and o.status == "PARTIAL"

def test_two_deliveries_close_line():
    o = make(); o.deliver(0, 3); o.deliver(0, 17); o.deliver(1, 5)
    assert o.status == "CLOSED"

def test_over_delivery_rejected():
    o = make()
    with pytest.raises(ValueError, match="exceeds open"):
        o.deliver(1, 6)
