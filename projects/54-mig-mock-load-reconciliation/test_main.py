from main import reconcile
L = [{"id": 1, "company": "CO01", "amount": 100.0}, {"id": 2, "company": "CO01", "amount": 50.0}, {"id": 3, "company": "MX01", "amount": 10.0}]
S = [{"id": 1, "company": "CO01", "amount": 100.0}, {"id": 2, "company": "CO01", "amount": 49.99}, {"id": 3, "company": "MX01", "amount": 10.0}, {"id": 9, "company": "MX01", "amount": 1.0}]
def test_reconciliation():
    r = reconcile(L, S)
    assert r["CO01"]["amount_mismatch"] == [2] and not r["CO01"]["ok"]
    assert r["MX01"]["extra_in_sap"] == [9]
