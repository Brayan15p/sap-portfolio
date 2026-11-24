import pytest
from decimal import Decimal
from main import cost

BOM = {"CREAM_50ML": {"base_qty": 100, "components": [("BULK_KG", 5, 2), ("JAR", 100, 1)]},
       "BULK_KG": {"base_qty": 1, "components": [("WATER", 0.7, 0), ("SHEA", 0.3, 0)]}}
PRICES = {"WATER": 1000, "SHEA": 60000, "JAR": 800}
ROUTING = {"BULK_KG": [("MIXER", 30)], "CREAM_50ML": [("FILLER", 120)]}
RATES = {"MIXER": 90000, "FILLER": 60000}

def test_two_level_cost_with_scrap_labor_overhead():
    c = cost("CREAM_50ML", BOM, PRICES, ROUTING, RATES)
    assert c["total"] > Decimal("1000") and c["labor"] > 0 and c["overhead"] > 0
    bulk = cost("BULK_KG", BOM, PRICES, ROUTING, RATES)
    assert bulk["material"] == Decimal("18700.00") and bulk["labor"] == Decimal("45000.00")

def test_recursive_bom_detected():
    bad = {"A": {"base_qty": 1, "components": [("B", 1, 0)]}, "B": {"base_qty": 1, "components": [("A", 1, 0)]}}
    with pytest.raises(ValueError, match="Recursive BOM: A > B > A"):
        cost("A", bad, {}, {}, {})
