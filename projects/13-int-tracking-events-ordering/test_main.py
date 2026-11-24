from main import Shipment

def test_old_event_does_not_regress():
    s = Shipment("G1", 4711)
    s.apply({"status": "DELIVERED", "ts": "2026-11-23T10:00"})
    assert s.apply({"status": "IN_TRANSIT", "ts": "2026-11-22T08:00"}) is False
    assert s.status == "DELIVERED" and len(s.history) == 2

def test_keeps_link_to_delivery():
    assert Shipment("G1", 4711).delivery_doc == 4711
