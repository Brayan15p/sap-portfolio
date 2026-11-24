from main import monitor
O = [{"qty": 10, "value": 500, "missing_fields": ["incoterms"]}, {"qty": 10, "value": 900, "credit_status": "B"},
     {"qty": 10, "value": 300, "confirmed_qty": 4}, {"qty": 1, "value": 50, "confirmed_qty": 1, "picked": True, "billed": True}]
def test_value_at_risk_by_reason():
    r = monitor(O)
    assert list(r)[0] == "credit_block" and r["not_confirmed"] == {"count": 1, "value": 300}
