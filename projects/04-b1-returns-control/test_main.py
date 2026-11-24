import pytest
from main import ReturnsLedger

def test_two_requests_respect_max():
    l = ReturnsLedger({(10, 0): 8})
    assert l.request(10, 0, 5, "damaged") == 3
    with pytest.raises(ValueError, match="Max returnable is 3"):
        l.request(10, 0, 4, "damaged")

def test_requires_origin_and_reason():
    l = ReturnsLedger({(10, 0): 8})
    with pytest.raises(KeyError): l.request(99, 0, 1, "x")
    with pytest.raises(ValueError): l.request(10, 0, 1, "")
