from main import landed_costs

ITEMS = {"MOTOR": {"qty": 10, "fob_usd": 500, "weight_kg": 40, "duty_pct": 5},
         "CABLE": {"qty": 1000, "fob_usd": 2, "weight_kg": 0.5, "duty_pct": 10}}

def test_exact_allocation_and_unit_cost():
    r = landed_costs(ITEMS, freight=3_000_000, insurance=300_000, handling=900_000, trm=4000)
    assert sum(v["freight"] for v in r.values()) == 3_000_000
    assert sum(v["handling"] for v in r.values()) == 900_000
    assert r["MOTOR"]["fob"] == 20_000_000 and r["CABLE"]["fob"] == 8_000_000

def test_heavy_item_takes_more_handling_cheap_item_higher_uplift():
    r = landed_costs(ITEMS, 3_000_000, 300_000, 900_000, 4000)
    assert r["CABLE"]["uplift_pct"] > r["MOTOR"]["uplift_pct"]
