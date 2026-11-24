from main import three_way_match

PO = {10: {"qty": 100, "price": 5000}, 20: {"qty": 10, "price": 80000}}

def test_clean_invoice_released():
    assert three_way_match(PO, {10: 100, 20: 10}, {10: {"qty": 100, "price": 5050}})["payment_block"] is False

def test_quantity_and_price_variance_block_payment():
    r = three_way_match(PO, {10: 60}, {10: {"qty": 100, "price": 5000}, 20: {"qty": 10, "price": 90000}})
    assert r["payment_block"] and "line 10: invoiced 100 > received 60" in r["issues"]
    assert any("12.5% above PO" in i for i in r["issues"])

def test_line_not_in_po():
    assert "line 30: not in purchase order" in three_way_match(PO, {}, {30: {"qty": 1, "price": 1}})["issues"]
