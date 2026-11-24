import pytest
from main import compare

CONV = {"UND": 1, "CAJA12": 12}

def test_box_vs_units_equivalent():
    r = compare([{"vendor": "A", "uom": "CAJA12", "price": 120}, {"vendor": "B", "uom": "UND", "price": 10}], CONV)
    assert r[0]["per_base_unit"] == r[1]["per_base_unit"] == 10

def test_freight_changes_ranking():
    r = compare([{"vendor": "A", "uom": "CAJA12", "price": 108, "freight": 30}, {"vendor": "B", "uom": "UND", "price": 10}], CONV)
    assert r[0]["vendor"] == "B"

def test_unknown_uom():
    with pytest.raises(ValueError): compare([{"vendor": "A", "uom": "KG", "price": 1}], CONV)
