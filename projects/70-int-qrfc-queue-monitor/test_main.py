from main import monitor
Q = {"CRM_ORDERS": [{"id": 1, "status": "READY", "ts": 0}, {"id": 2, "status": "SYSFAIL", "error": "Customer 4711 locked", "ts": 60}] + [{"id": i, "status": "READY", "ts": 100} for i in range(3, 503)],
     "IDOC_OUT": [{"id": 1, "status": "READY", "ts": 0}]}
def test_blocked_queue_first():
    r = monitor(Q, now=3600)
    assert r[0] == {"queue": "CRM_ORDERS", "state": "BLOCKED", "blocking_entry": 2, "error": "Customer 4711 locked", "waiting": 500, "oldest_age_min": 60}
    assert r[1]["state"] == "SLOW"
