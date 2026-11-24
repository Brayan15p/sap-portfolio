from main import exposure
I = [{"kind": "AP", "ccy": "USD", "amount": 1_000_000, "days": 30}, {"kind": "AR", "ccy": "USD", "amount": 200_000, "days": 60},
     {"kind": "AP", "ccy": "USD", "amount": 400_000, "days": 120}, {"kind": "AP", "ccy": "EUR", "amount": 100_000, "days": 400}]
def test_net_and_policy():
    b, p = exposure(I)
    assert {"ccy": "USD", "bucket": "0-90", "net_exposure": -800_000, "buy_forward": 600_000.0} in p
    assert any(x["bucket"] == "91-180" and x["buy_forward"] == 200_000.0 for x in p) and len(p) == 2
