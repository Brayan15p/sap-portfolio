from datetime import date
from main import forecast

START = date(2026, 11, 23)

def test_late_payer_shifts_collection_and_triggers_alert():
    ar = [{"customer": "SLOW", "due": date(2026, 11, 30), "amount": 50_000_000}]
    ap = [{"due": date(2026, 12, 1), "amount": 40_000_000}]
    weeks, alert = forecast(30_000_000, START, ar, ap, 5_000_000, {"SLOW": 45}, minimum=10_000_000)
    assert weeks[1]["in"] == 0 and weeks[7]["in"] == 50_000_000
    assert alert == 2

def test_on_time_payer_no_alert():
    ar = [{"customer": "GOOD", "due": date(2026, 11, 30), "amount": 50_000_000}]
    _, alert = forecast(30_000_000, START, ar, [], 1_000_000, {}, minimum=10_000_000)
    assert alert is None
