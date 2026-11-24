import pytest
from main import gstin_valid, gst

def test_published_gstins_validate():
    assert gstin_valid("27AAPFU0939F1ZV") and gstin_valid("29AAGCB7383J1Z4")
    assert not gstin_valid("27AAPFU0939F1ZX")

def test_intrastate_vs_interstate():
    assert gst("27AAPFU0939F1ZV", "27AAPFU0939F1ZV", 10000, 18) == {"CGST": 900.0, "SGST": 900.0, "IGST": 0.0, "total": 11800.0}
    assert gst("27AAPFU0939F1ZV", "29AAGCB7383J1Z4", 10000, 18)["IGST"] == 1800.0

def test_invalid_gstin_blocks():
    with pytest.raises(ValueError): gst("27AAPFU0939F1ZX", "29AAGCB7383J1Z4", 1, 18)
