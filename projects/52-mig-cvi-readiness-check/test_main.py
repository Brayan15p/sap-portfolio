from main import readiness
def test_report_per_record_and_rule():
    r = readiness([{"id": "1", "name": "A", "country": "CO", "tax_id": "900123456"},
                   {"id": "2", "name": "", "country": "Colombia", "email": "bad@"},
                   {"id": "3", "name": "C", "country": "US", "postal": "ABC"}])
    assert r["ready_pct"] == 33.3 and r["failures"]["2"] == ["name", "country", "email_format"]
    assert r["by_rule"]["postal_code_for_US"] == 1
