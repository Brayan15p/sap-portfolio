from main import replenish
S = {"S1": {"avg_daily": 10, "safety": 10, "on_hand": 20, "in_transit": 0, "case_pack": 12, "shelf_capacity": 200},
     "S2": {"avg_daily": 10, "safety": 10, "on_hand": 20, "in_transit": 0, "case_pack": 12, "shelf_capacity": 60}}
def test_promo_uplift_and_shelf_cap():
    r = replenish(S, {"S1": 1.0, "S2": 1.0}, days_cover=3)
    assert r["S1"] == 60 and r["S2"] == 36
    assert replenish(S, {}, 3)["S1"] == 24
