def assess(costs, cycles):
    """costs: {cc: amount}. cycles: [(sender, {receiver: driver})] executed in order."""
    costs = dict(costs)
    for sender, drivers in cycles:
        amount = costs.get(sender, 0)
        total_driver = sum(drivers.values())
        if total_driver == 0:
            raise ValueError(f"Sender {sender} has no driver quantities")
        shares = {r: round(amount * d / total_driver) for r, d in drivers.items()}
        # put the rounding difference on the largest receiver so totals tie out exactly
        diff = amount - sum(shares.values())
        shares[max(drivers, key=drivers.get)] += diff
        for r, v in shares.items():
            costs[r] = costs.get(r, 0) + v
        costs[sender] = 0
    return costs
