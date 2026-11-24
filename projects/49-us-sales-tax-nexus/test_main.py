from main import nexus

def test_rules_and_or_sales():
    orders = [{"state": "GA", "amount": 100} for _ in range(200)] + \
             [{"state": "NY", "amount": 6000} for _ in range(90)] + \
             [{"state": "CA", "amount": 410_000}]
    s = nexus(orders)
    assert s["GA"] == "NEXUS"       # 200 transactions, OR rule
    assert s["NY"] == "WARNING"     # sales over threshold but only 90 tx, AND rule
    assert s["CA"] == "WARNING"
