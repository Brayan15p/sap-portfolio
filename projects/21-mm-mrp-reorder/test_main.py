import pytest
from main import mrp

def test_proposal_respects_lot_and_rounding_and_safety():
    props, proj = mrp(stock=100, safety=40, daily_demand=[20]*10, open_pos={}, lead_time=2, horizon=10, min_lot=50, rounding=24)
    assert props[0] == (1, 3, 72)  # day 3 level 40-20=... below 40, lot 50 rounded to 72
    assert min(proj) >= 40

def test_open_po_avoids_proposal():
    props, _ = mrp(100, 40, [20]*5, {2: 100}, 2, 5, 50, 1)
    assert props == []

def test_impossible_lead_time_raises():
    with pytest.raises(RuntimeError, match="expedite"):
        mrp(30, 40, [20]*5, {}, 3, 5, 10, 1)
