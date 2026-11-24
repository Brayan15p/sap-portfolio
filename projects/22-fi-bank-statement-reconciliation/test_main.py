from main import reconcile

OPEN = [{"ref": "FE-1001", "amount": 500000}, {"ref": "FE-1002", "amount": 300000}, {"ref": "FE-1003", "amount": 300000}]
ST = [{"id": 1, "text": "TRANSF CLIENTE ABC FE1001", "amount": 500000},
      {"id": 2, "text": "GMF 4X1000", "amount": -2000},
      {"id": 3, "text": "CONSIGNACION", "amount": 300000},
      {"id": 4, "text": "PAGO FE-1002 PARCIAL", "amount": 100000}]

def test_full_day():
    posted, work = reconcile(ST, OPEN)
    assert {"line": 1, "invoice": "FE-1001", "status": "CLEARED"} in posted
    assert {"line": 2, "account": "Bank charges", "amount": 2000} in posted
    assert {"line": 4, "invoice": "FE-1002", "status": "PARTIAL"} in posted
    assert work == [{"line": 3, "reason": "ambiguous amount"}]
