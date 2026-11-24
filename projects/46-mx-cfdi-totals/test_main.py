import pytest
from decimal import Decimal
from main import rfc_valid, cfdi_totals

def test_rfc_types():
    assert rfc_valid("ABC010203XY1") == "PERSONA_MORAL"
    assert rfc_valid("GOMA850101AB1") == "PERSONA_FISICA"
    assert rfc_valid("GOMA851301AB1") is None   # month 13

def test_company_to_company():
    t = cfdi_totals([{"qty": 2, "unit": "1000", "discount": "100"}], "ABC010203XY1", "XYZ990101AB2")
    assert t["Total"] == Decimal("2204.00")

def test_individual_to_company_withholdings():
    t = cfdi_totals([{"qty": 1, "unit": "10000"}], "GOMA850101AB1", "XYZ990101AB2")
    assert t["TotalImpuestosRetenidos"] == Decimal("2066.67") and t["Total"] == Decimal("9533.33")
