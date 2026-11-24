from main import classify
I = {"A1": {"demand": [100, 100, 100, 100], "price": 100}, "B1": {"demand": [10, 30, 20, 20], "price": 50},
     "C1": {"demand": [0, 10, 0, 0], "price": 10}}
def test_abc_xyz():
    r = classify(I)
    assert r["A1"] == "AX" and r["C1"].endswith("Z")
