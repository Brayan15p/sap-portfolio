from main import read_cost, recommend
def test_growth_rates():
    keys = list(range(0, 10000, 100))
    s, so, h = (read_cost(k, 10000, keys) for k in ("STANDARD", "SORTED", "HASHED"))
    assert s > 50 * so and so > h and h == 100
def test_recommendation():
    assert recommend(True, False, True) == "HASHED" and recommend(False, True, True) == "SORTED"
