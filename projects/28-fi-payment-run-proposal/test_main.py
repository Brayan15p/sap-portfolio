from datetime import date
from main import proposal

ITEMS = [{"id": "A", "vendor": "V1", "amount": 1_000_000, "due": date(2026, 12, 20), "disc_pct": 2, "disc_date": date(2026, 11, 30)},
         {"id": "B", "vendor": "V2", "amount": 500_000, "due": date(2026, 11, 25)},
         {"id": "C", "vendor": "V3", "amount": 700_000, "due": date(2026, 11, 26)},
         {"id": "D", "vendor": "V4", "amount": 100_000, "due": date(2026, 11, 20)}]

def test_discount_priority_blocked_and_limit():
    paid, exc, total = proposal(ITEMS, date(2026, 11, 27), date(2026, 12, 4), 1_600_000, blocked_vendors={"V4"})
    assert [p["id"] for p in paid] == ["A", "B"] and paid[0]["pay"] == 980_000
    assert ("D", "blocked") in exc and ("C", "bank limit") in exc and total == 1_480_000
