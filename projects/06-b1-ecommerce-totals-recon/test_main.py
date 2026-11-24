from main import reconcile

def test_match():
    d = {"subtotal": 100, "discount": 10, "tax": 17.1, "total": 107.1}
    assert reconcile(d, dict(d))["status"] == "MATCH"

def test_tax_difference_identified():
    shop = {"subtotal": 100, "discount": 0, "tax": 19, "total": 119}
    b1 = {"subtotal": 100, "discount": 0, "tax": 5, "total": 105}
    assert reconcile(shop, b1)["causes"] == [{"component": "tax", "diff": 14}]

def test_rounding_residual():
    shop = {"subtotal": 100, "discount": 0, "tax": 19, "total": 119.04}
    b1 = {"subtotal": 100, "discount": 0, "tax": 19, "total": 119}
    assert reconcile(shop, b1)["causes"][-1]["component"] == "rounding"
