from datetime import date
from main import provision
S = [{"material": "M1", "qty": 10, "unit_cost": 100, "last_issue": date(2025, 10, 1)},
     {"material": "M2", "qty": 10, "unit_cost": 100, "last_issue": date(2026, 7, 1)},
     {"material": "M3", "qty": 1, "unit_cost": 50, "last_issue": date(2026, 11, 20), "expiry": date(2026, 11, 1)}]
def test_buckets_and_entry():
    rows, total, entry = provision(S, date(2026, 11, 23))
    assert [r["bucket"] for r in rows] == ["OBSOLETE", "SLOW_90", "EXPIRED"] and total == 1250.0
    assert entry[0][1] == entry[1][2]
