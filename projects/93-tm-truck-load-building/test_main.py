from main import build_loads
D = [{"id": i, "kg": kg, "m3": m3} for i, (kg, m3) in enumerate([(4000, 10), (3000, 20), (2000, 5), (1000, 15), (5000, 8), (500, 2)])]
def test_fewest_trucks_within_limits():
    L = build_loads(D, max_kg=10000, max_m3=40)
    assert len(L) == 2 and all(l["kg"] <= 10000 and l["m3"] <= 40 for l in L)
