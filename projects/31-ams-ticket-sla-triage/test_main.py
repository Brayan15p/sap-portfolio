from datetime import datetime
from main import sla_state

def test_weekend_does_not_count():
    t = {"impact": "HIGH", "urgency": "MEDIUM", "opened": datetime(2026, 11, 20, 16, 0)}  # Friday 16:00
    s = sla_state(t, datetime(2026, 11, 23, 12, 0))  # Monday 12:00 -> 2h Fri + 4h Mon
    assert s["priority"] == "P2" and s["used_h"] == 6 and s["state"] == "OK"

def test_escalate_and_pause():
    t = {"impact": "HIGH", "urgency": "HIGH", "opened": datetime(2026, 11, 23, 8, 0)}
    assert sla_state(t, datetime(2026, 11, 23, 11, 30))["state"] == "ESCALATE"
    t["pauses"] = [(datetime(2026, 11, 23, 9, 0), datetime(2026, 11, 23, 11, 0))]
    assert sla_state(t, datetime(2026, 11, 23, 11, 30))["state"] == "OK"
