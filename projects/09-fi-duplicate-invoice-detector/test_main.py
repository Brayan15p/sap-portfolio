from datetime import date
from main import find_duplicates

def inv(i, ref, d, amt=1000, v="V1"):
    return {"id": i, "vendor": v, "ref": ref, "amount": amt, "date": d}

def test_formatting_variants_are_caught():
    h = find_duplicates([inv(1, "FE-00123", date(2026, 1, 1)), inv(2, "fe 123", date(2026, 3, 1))])
    assert h[0]["pair"] == (1, 2) and "same normalized reference" in h[0]["reasons"]

def test_different_amount_not_flagged():
    assert find_duplicates([inv(1, "A1", date(2026, 1, 1)), inv(2, "A1", date(2026, 1, 1), amt=999)]) == []
