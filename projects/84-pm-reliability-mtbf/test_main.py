from main import reliability
E = {"MRI-01": [{"repair_h": 10}, {"repair_h": 14}, {"repair_h": 6}], "CHILLER-02": [{"repair_h": 4}], "PUMP-03": []}
def test_ranking_by_risk():
    r = reliability(E, 8760, 720, {"MRI-01": 10, "CHILLER-02": 8, "PUMP-03": 3})
    assert list(r)[0] == "MRI-01" and r["MRI-01"]["mtbf_h"] == 2910.0 and r["PUMP-03"]["p_fail_next"] == 0.0
