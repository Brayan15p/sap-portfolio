from datetime import date
from main import revalue

def test_ap_loss_when_peso_weakens_and_reversal_next_day():
    e = revalue([{"id": "AP1", "kind": "AP", "usd": 10000, "booked_rate": "4000"}], "4150", date(2026, 11, 30))
    assert e[0] == {"item": "AP1", "date": date(2026, 11, 30), "account": "Unrealized FX loss", "amount": 1_500_000}
    assert e[1]["date"] == date(2026, 12, 1) and e[1]["amount"] == -1_500_000

def test_ar_gain():
    e = revalue([{"id": "AR1", "kind": "AR", "usd": 1000, "booked_rate": "4000"}], "4100", date(2026, 11, 30))
    assert e[0]["account"] == "Unrealized FX gain" and e[0]["amount"] == 100_000
