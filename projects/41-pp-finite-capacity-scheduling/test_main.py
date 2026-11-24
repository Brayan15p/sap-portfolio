from main import schedule

CAP = {"CUT": 8, "WELD": 4, "PAINT": 8}

def test_capacity_never_exceeded():
    orders = [{"id": f"O{i}", "due": 10, "ops": [("CUT", 6), ("WELD", 6), ("PAINT", 4)]} for i in range(3)]
    _, _, load = schedule(orders, CAP)
    assert all(h <= CAP[wc] for (wc, _), h in load.items())

def test_late_order_flags_bottleneck():
    orders = [{"id": "BIG", "due": 2, "ops": [("CUT", 8), ("WELD", 16), ("PAINT", 8)]}]
    _, late, _ = schedule(orders, CAP)
    assert late and late[0]["bottleneck"] == "WELD"
