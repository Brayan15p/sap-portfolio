import pytest
from datetime import date
from main import CreditCheck

AR = [{"customer": "C1", "open": 6_000_000, "due": date(2026, 10, 1)}]
OO = [{"customer": "C1", "amount": 2_000_000}]

def test_blocked_by_limit_and_overdue():
    c = CreditCheck({"C1": 10_000_000})
    r = c.check({"id": "O1", "customer": "C1", "amount": 3_000_000}, AR, OO, date(2026, 11, 23))
    assert r["status"] == "BLOCKED" and len(r["reasons"]) == 2 and r["exposure"] == 11_000_000

def test_within_limit_ok():
    c = CreditCheck({"C1": 20_000_000}, max_overdue_days=60)
    assert c.check({"id": "O1", "customer": "C1", "amount": 1}, AR, OO, date(2026, 11, 23))["status"] == "OK"

def test_release_once_with_reason():
    c = CreditCheck({"C1": 1}); c.release("O1", "jefe.cartera", "pago confirmado por transferencia")
    assert c.check({"id": "O1", "customer": "C1", "amount": 5}, AR, OO, date(2026, 11, 23))["status"] == "RELEASED"
    with pytest.raises(ValueError): c.release("O1", "x", "y")
