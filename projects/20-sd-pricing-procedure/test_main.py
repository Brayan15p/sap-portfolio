from decimal import Decimal
from main import price

REC = {"PR00": {("mat", "ARROZ"): "100000", ("pricelist", "MAYOR", "ARROZ"): "95000", ("cust_mat", "C9", "ARROZ"): "90000"},
       "customer_pricelist": {"C1": "MAYOR"}, "K007": {"C1": 5}, "scales": {"ARROZ": [(10, 2), (50, 4)]}, "MWST": 19}

def total(steps): return steps[-1][2]

def test_access_sequence_most_specific_wins():
    assert price("ARROZ", 1, "C9", REC)[0][1] == "cust_mat"
    assert price("ARROZ", 1, "C1", REC)[0][1] == "pricelist"
    assert price("ARROZ", 1, "C2", REC)[0][1] == "mat"

def test_discount_scale_and_tax():
    s = price("ARROZ", 50, "C1", REC)
    # 95000*50=4,750,000 -5% =4,512,500 -4% =4,332,000 +19% =5,155,080
    assert total(s) == Decimal("5155080.00")
