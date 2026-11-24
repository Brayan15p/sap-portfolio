from datetime import date
from main import analyze
L = [{"po": "4500/10", "gr_qty": 10, "ir_qty": 0, "po_price": 100, "ir_value": 0, "last_movement": date(2026, 11, 1)},
     {"po": "4501/10", "gr_qty": 5, "ir_qty": 5, "po_price": 100, "ir_value": 550, "last_movement": date(2026, 6, 1)},
     {"po": "4502/10", "gr_qty": 1, "ir_qty": 1, "po_price": 10, "ir_value": 10, "last_movement": date(2026, 6, 1)}]
def test_classification_and_aging():
    r = analyze(L, date(2026, 11, 23))
    assert r[0]["kind"] == "GR_NOT_INVOICED" and r[1]["kind"] == "PRICE_DIFFERENCE"
    assert r[1]["action"].startswith("write-off") and len(r) == 2
