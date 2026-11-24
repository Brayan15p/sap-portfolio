from main import apply_payment
OPEN = [{"ref": "1001", "amount": 500.0, "due": 1}, {"ref": "1002", "amount": 300.0, "due": 2}, {"ref": "1003", "amount": 200.0, "due": 3},
        {"ref": "1004", "amount": 800.0, "due": 4}]
def test_exact_combination_prefers_note():
    assert apply_payment(800.0, OPEN, note="pago facturas 1002 y 1001")["invoices"] == ["1001", "1002"]
    assert apply_payment(800.0, OPEN)["invoices"] == ["1004"] or apply_payment(800.0, OPEN)["status"] == "MATCHED"
    assert apply_payment(123.0, OPEN)["status"] == "UNAPPLIED"
