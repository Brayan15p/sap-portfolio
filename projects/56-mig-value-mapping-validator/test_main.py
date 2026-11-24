from main import validate
def test_conflict_unmapped_unused():
    r = validate([("30D", "Z030"), ("30D", "Z031"), ("CONT", "Z000"), ("90D", "Z090")],
                 [{"terms": "30D"}, {"terms": "CONT"}, {"terms": "45D"}, {"terms": "45D"}], "terms")
    assert "conflict: 30D -> Z030 and Z031" in r["problems"] and "unmapped value '45D' used in 2 rows" in r["problems"]
    assert r["unused_mappings"] == ["90D"]
