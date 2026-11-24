from datetime import date
from main import open_items_at

INV = [{"id": "F1", "amount": 1000, "posting": date(2026, 9, 1)},
       {"id": "F2", "amount": 300, "posting": date(2026, 10, 15)}]
CLR = [{"invoice": "F1", "amount": 1000, "date": date(2026, 10, 5)}]

def test_payment_after_key_date_ignored():
    assert open_items_at(INV, CLR, date(2026, 9, 30)) == {"F1": 1000}

def test_after_payment():
    assert open_items_at(INV, CLR, date(2026, 10, 31)) == {"F2": 300}
