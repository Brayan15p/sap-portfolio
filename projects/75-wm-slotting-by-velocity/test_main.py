from main import slot, walking
SK = {"FAST": (1000, 1.0), "MID": (200, 1.0), "SLOW": (10, 1.0)}
B = {"B01": (5, 2), "B02": (20, 2), "B03": (60, 2)}
def test_fast_movers_closest_and_saving():
    a = slot(SK, B)
    assert a["FAST"] == "B01" and a["SLOW"] == "B03"
    worst = walking({"FAST": "B03", "MID": "B02", "SLOW": "B01"}, SK, B)
    assert walking(a, SK, B) < worst / 5
