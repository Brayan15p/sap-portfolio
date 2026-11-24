from decimal import Decimal
from main import compare
def test_markdowns_change_ratio_and_gap_is_explained():
    r = compare({"DAIRY": {"opening_cost": 600, "purchases_cost": 1400, "opening_retail": 1000, "purchases_retail": 2000, "markdowns": 500,
                           "sales_retail": 1500, "actual_ending_cost": 820}})["DAIRY"]
    assert r["cost_ratio"] == 0.8 and r["retail_method_value"] == Decimal("800.00") and r["gap"] == Decimal("-20.00")
