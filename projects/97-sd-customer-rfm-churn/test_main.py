from datetime import date, timedelta
from main import rfm
T = date(2026, 11, 23)
O = [{"customer": "LOYAL", "date": T - timedelta(days=d), "amount": 100} for d in range(1, 60, 5)] + \
    [{"customer": "GONE", "date": T - timedelta(days=d), "amount": 100} for d in range(200, 300, 10)] + \
    [{"customer": "NEWBIE", "date": T - timedelta(days=2), "amount": 50}] + \
    [{"customer": f"X{i}", "date": T - timedelta(days=100 + i), "amount": 10} for i in range(5)]
def test_segments():
    r = rfm(O, T)
    assert r["LOYAL"]["segment"] == "CHAMPION" and r["GONE"]["segment"] == "AT_RISK" and r["NEWBIE"]["segment"] == "NEW"
