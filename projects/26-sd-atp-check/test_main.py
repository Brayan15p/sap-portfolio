from main import atp

def test_partial_now_rest_after_receipt():
    conf, rest = atp(stock=100, receipts={5: 80}, commitments={1: 30}, req_qty=120, req_day=3)
    assert conf == [(3, 70), (5, 50)] and rest == 0

def test_does_not_steal_future_commitment():
    conf, _ = atp(stock=100, receipts={}, commitments={10: 60}, req_qty=80, req_day=1)
    assert conf == [(1, 40)]
