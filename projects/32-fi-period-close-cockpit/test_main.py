import pytest
from main import Close

T = {"GRIR": {"deps": [], "critical": True}, "FX": {"deps": ["GRIR"], "critical": True},
     "DEPR": {"deps": [], "critical": True}, "REPORTS": {"deps": ["FX", "DEPR"], "critical": False}}

def test_dependencies_and_close():
    c = Close(T)
    assert c.ready() == ["DEPR", "GRIR"]
    with pytest.raises(ValueError, match="blocked"): c.complete("FX", "x")
    for t in ["GRIR", "FX", "DEPR"]: c.complete(t, f"{t}.pdf")
    assert c.close_period() == "PERIOD CLOSED"

def test_critical_pending_and_cycle():
    with pytest.raises(ValueError, match="critical tasks pending"): Close(T).close_period()
    with pytest.raises(ValueError, match="cycle"): Close({"A": {"deps": ["B"], "critical": 0}, "B": {"deps": ["A"], "critical": 0}})
