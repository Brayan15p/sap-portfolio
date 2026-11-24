from main import net
P = [("CO", "MX", 100), ("MX", "US", 80), ("US", "CO", 50), ("BR", "CO", 30), ("MX", "BR", 20), ("US", "MX", 10)]
def test_fewer_transfers_same_positions():
    pos, tr = net(P)
    assert sum(pos.values()) == 0 and len(tr) < len(P)
    applied = {e: 0 for e in pos}
    for f, t, a in tr: applied[f] -= a; applied[t] += a
    assert applied == pos
