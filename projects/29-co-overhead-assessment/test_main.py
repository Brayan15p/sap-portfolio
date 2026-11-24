import pytest
from main import assess

def test_two_cycles_total_preserved_sender_zero():
    start = {"IT": 1_000_000, "MANT": 500_000, "URG": 0, "UCI": 0, "LAB": 0}
    r = assess(start, [("IT", {"URG": 3, "UCI": 3, "LAB": 1, "MANT": 2}), ("MANT", {"URG": 120, "UCI": 80, "LAB": 50})])
    assert r["IT"] == 0 and r["MANT"] == 0 and sum(r.values()) == 1_500_000

def test_no_driver():
    with pytest.raises(ValueError): assess({"IT": 1}, [("IT", {"A": 0})])
