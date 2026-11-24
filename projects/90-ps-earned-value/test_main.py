from main import evm
W = {"1.1 Foundations": {"bac": 1000, "pv": 600, "ac": 700, "pct_complete": 0.5}, "1.2 Structure": {"bac": 2000, "pv": 200, "ac": 180, "pct_complete": 0.1}}
def test_evm_metrics():
    r = evm(W)
    assert r["1.1 Foundations"] == {"EV": 500, "CPI": 0.71, "SPI": 0.83, "EAC": 1400, "VAC": -400, "status": "RED"}
    assert r["1.2 Structure"]["status"] == "GREEN"
