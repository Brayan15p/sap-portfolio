import pytest
from main import Hub

def make():
    h = Hub(max_attempts=3, base_delay=10); got = {"carrier": [], "shop": []}
    h.subscribe("carrier", lambda e: got["carrier"].append(e["doc"]))
    h.subscribe("shop", lambda e: got["shop"].append(e["doc"]))
    return h, got

def test_each_subscriber_gets_event_exactly_once():
    h, got = make(); h.post_delivery("DN1", {"qty": 5})
    h.relay(now=0); h.relay(now=1000)
    assert got == {"carrier": ["DN1"], "shop": ["DN1"]} and h.status() == {"DONE": 2}

def test_one_subscriber_down_retries_with_backoff_others_unaffected():
    h, got = make(); calls = []
    def flaky(e):
        calls.append(1)
        if len(calls) < 3: raise ConnectionError("BI down")
    h.subscribe("bi", flaky); h.post_delivery("DN2", {})
    h.relay(now=0); h.relay(now=5)          # second call too early: backoff 10s
    assert len(calls) == 1
    h.relay(now=10); h.relay(now=30)
    assert len(calls) == 3 and h.status()["DONE"] == 3

def test_poison_message_goes_to_dead_letter():
    h, _ = make(); h.subscribe("bad", lambda e: 1 / 0); h.post_delivery("DN3", {})
    for t in (0, 10, 30): h.relay(now=t)
    assert h.status()["DEAD"] == 1

def test_business_write_and_event_are_atomic():
    h, _ = make(); h.post_delivery("DN4", {})
    with pytest.raises(Exception): h.post_delivery("DN4", {})   # duplicate doc
    assert h.db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0] == 1
