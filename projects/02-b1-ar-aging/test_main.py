from datetime import date
from main import aging

INV = [
    {"id": 1, "customer": "C1", "due": date(2026, 10, 1), "amount": 1000},
    {"id": 2, "customer": "C1", "due": date(2026, 11, 20), "amount": 500},
    {"id": 3, "customer": "C2", "due": date(2026, 12, 15), "amount": 300},
]

def test_partial_payment_only_open_balance():
    r = aging(INV, [{"invoice_id": 1, "amount": 400}], date(2026, 11, 23))
    assert r["C1"]["31-60"] == 600

def test_fully_paid_disappears():
    r = aging(INV, [{"invoice_id": 2, "amount": 500}], date(2026, 11, 23))
    assert "0-30" not in r["C1"]

def test_not_due_bucket():
    assert aging(INV, [], date(2026, 11, 23))["C2"] == {"not due": 300}
