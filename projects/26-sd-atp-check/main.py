def atp(stock, receipts, commitments, req_qty, req_day, horizon=30):
    """receipts/commitments: {day: qty}. Returns confirmations [(day, qty)]."""
    def cum_available(day):
        return stock + sum(q for d, q in receipts.items() if d <= day) - sum(q for d, q in commitments.items())
    # what is free on a day must also stay free for later commitments: take the minimum of future cumulative availability
    def free_on(day):
        return min(cum_available(d) for d in range(day, horizon + 1))
    confirmations, remaining, taken = [], req_qty, 0
    for day in range(req_day, horizon + 1):
        avail = free_on(day) - taken
        if avail > 0:
            q = min(avail, remaining); confirmations.append((day, q)); taken += q; remaining -= q
        if remaining == 0: break
    return confirmations, remaining
