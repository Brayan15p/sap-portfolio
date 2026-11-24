from main import anomalies
def test_detects_slow_run_ignores_normal_noise():
    h = {"Z_MRP": [20, 22, 19, 21, 20, 23, 60], "Z_BILL": [5, 6, 5, 7, 6]}
    r = anomalies(h, {"Z_MRP": 180, "Z_BILL": 7})
    assert [x["job"] for x in r] == ["Z_MRP"]
