def net(payables):
    """payables: [(from, to, amount)] in group currency"""
    pos = {}
    for f, t, a in payables: pos[f] = pos.get(f, 0) - a; pos[t] = pos.get(t, 0) + a
    payers = sorted([[e, -v] for e, v in pos.items() if v < 0], key=lambda x: -x[1])
    receivers = sorted([[e, v] for e, v in pos.items() if v > 0], key=lambda x: -x[1])
    transfers = []
    while payers and receivers:
        p, r = payers[0], receivers[0]; amt = min(p[1], r[1])
        transfers.append((p[0], r[0], amt)); p[1] -= amt; r[1] -= amt
        if p[1] == 0: payers.pop(0)
        if r[1] == 0: receivers.pop(0)
    return pos, transfers
