from main import score
SUP = {"S_CN": {"country": "CN", "on_time": 0.7, "financial_alert": True}, "S_CO": {"country": "CO", "on_time": 0.95, "financial_alert": False}}
SRC = {"CHIP": ["S_CN"], "RESIN": ["S_CN"], "BOX": ["S_CO", "S_CN"], "LABEL": ["S_CO"]}
def test_risk_and_single_source():
    r = score(SUP, SRC)
    assert list(r)[0] == "S_CN" and r["S_CN"]["level"] == "HIGH" and r["S_CN"]["single_sourced"] == ["CHIP", "RESIN"]
