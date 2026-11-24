from main import determine

def test_four_scenarios():
    assert determine("ES", "ES", None, 0, 100)["vat"] == 21
    assert determine("ES", "DE", "DE123456789", 0, 100)["code"] == "REVERSE_CHARGE"
    assert determine("ES", "FR", None, 20_000, 100) == {"code": "OSS", "rate": 20, "vat": 20.0, "note": "OSS, FR rate"}
    assert determine("ES", "US", None, 0, 100)["code"] == "EXPORT"

def test_threshold_crossing_switches_to_destination():
    assert determine("ES", "DE", None, 9_950, 40)["code"] == "B2C_ORIGIN"
    assert determine("ES", "DE", None, 9_950, 60)["code"] == "OSS"
