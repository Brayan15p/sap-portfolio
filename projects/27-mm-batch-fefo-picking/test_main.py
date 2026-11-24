import pytest
from datetime import date
from main import pick

B = [{"batch": "L3", "expiry": date(2027, 6, 1), "qty": 50, "status": "UNRESTRICTED"},
     {"batch": "L1", "expiry": date(2026, 12, 10), "qty": 40, "status": "UNRESTRICTED"},
     {"batch": "L0", "expiry": date(2026, 11, 30), "qty": 100, "status": "UNRESTRICTED"},
     {"batch": "L2", "expiry": date(2027, 1, 1), "qty": 30, "status": "QUALITY_BLOCK"}]

def test_fefo_skips_short_shelf_life_and_blocked():
    assert pick(B, 60, date(2026, 11, 1)) == [("L1", 40), ("L3", 20)]

def test_shortage_message():
    with pytest.raises(ValueError, match="Short by 10"):
        pick(B, 100, date(2026, 11, 1))
