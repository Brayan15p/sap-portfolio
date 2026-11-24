from main import evaluate

D = [{"vendor": "A", "days_late": 0, "qty": 100, "rejected": 0}, {"vendor": "A", "days_late": 5, "qty": 100, "rejected": 10},
     {"vendor": "B", "days_late": 0, "qty": 100, "rejected": 0}, {"vendor": "B", "days_late": -1, "qty": 100, "rejected": 0}]

def test_cheapest_is_not_automatically_best():
    r = evaluate(D, {"A": 90, "B": 100})
    assert list(r)[0] == "B" and r["A"]["on_time"] == 50.0 and r["A"]["quality"] == 95.0

def test_threshold_flags_review():
    assert evaluate(D, {"A": 90, "B": 100}, threshold=90)["A"]["review"] is True
