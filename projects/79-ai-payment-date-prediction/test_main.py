from datetime import date
from main import predict
def test_recent_behavior_weighs_more():
    worsening = predict([0, 0, 0, 0, 30, 30, 30], date(2026, 12, 1))
    assert worsening["expected_delay"] > 15
def test_consistent_payer_high_reliability():
    r = predict([10, 11, 9, 10, 12, 10], date(2026, 12, 1))
    assert r["reliability"] == "HIGH" and r["date"] == date(2026, 12, 11)
