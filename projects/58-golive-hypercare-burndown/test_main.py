from main import hypercare
def test_alert_and_eta():
    d = [{"opened": 40, "closed": 10}, {"opened": 35, "closed": 20}, {"opened": 30, "closed": 25}, {"opened": 20, "closed": 30}, {"opened": 10, "closed": 30}, {"opened": 10, "closed": 25}]
    r = hypercare(d)
    assert r["alert_day"] == 3 and r["rows"][2]["backlog"] == 50 and r["rows"][-1]["backlog"] == 5 and r["days_to_clear"] == 0.3
