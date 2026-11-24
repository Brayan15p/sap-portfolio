from main import decide, oc_curve
def test_decision_and_oc_curve_monotonic():
    assert decide(1, 1) == "ACCEPT" and decide(2, 1) == "REJECT"
    oc = oc_curve(50, 1)
    vals = list(oc.values()); assert vals == sorted(vals, reverse=True)
    assert oc[0.01] > 0.9 and oc[0.10] < 0.05
