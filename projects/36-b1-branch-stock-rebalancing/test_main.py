from main import rebalance

S = {"BOG": 500, "MED": 20, "CAL": 300, "BAQ": 10}
T = {"BOG": 200, "MED": 150, "CAL": 150, "BAQ": 120}
SS = {"BOG": 250, "MED": 50, "CAL": 100, "BAQ": 50}
C = {("BOG", "MED"): 300, ("CAL", "MED"): 200, ("BOG", "BAQ"): 500, ("CAL", "BAQ"): 700}

def test_cheapest_route_first_and_safety_respected():
    m = rebalance(S, T, SS, C)
    assert m[0] == ("CAL", "MED", 130)
    sent = {w: sum(q for f, _, q in m if f == w) for w in S}
    assert S["BOG"] - sent["BOG"] >= SS["BOG"] and S["CAL"] - sent["CAL"] >= T["CAL"]

def test_all_deficits_covered_when_possible():
    m = rebalance(S, T, SS, C)
    got = {w: sum(q for _, t, q in m if t == w) for w in S}
    assert got["MED"] == 130 and got["BAQ"] == 110
