from main import allocate
D = [{"id": "DN1", "kg": 1000, "m3": 2}, {"id": "DN2", "kg": 100, "m3": 4}, {"id": "DN3", "kg": 500, "m3": 1}]
def test_volumetric_and_exact_total():
    s = allocate(1_000_001, D)
    assert sum(s.values()) == 1_000_001 and s["DN1"] > s["DN2"] > s["DN3"]
