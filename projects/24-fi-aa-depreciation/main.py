from decimal import Decimal, ROUND_HALF_UP

def q(x): return Decimal(x).quantize(Decimal("0.01"), ROUND_HALF_UP)

def schedule(cost, salvage, life_months, cap_month, months, retirements=None):
    """retirements: {month: fraction retired}. Returns [(month, depreciation, net_book_value)]."""
    cost, salvage = Decimal(cost), Decimal(salvage)
    acc = Decimal(0); out = []
    retirements = retirements or {}
    for m in range(cap_month, cap_month + months):
        if m in retirements:
            f = Decimal(str(retirements[m]))
            cost, salvage, acc = cost * (1 - f), salvage * (1 - f), acc * (1 - f)
        if m == cap_month:  # depreciation starts the month after capitalization
            out.append((m, q(0), q(cost - acc))); continue
        monthly = (cost - salvage) / life_months
        dep = min(monthly, cost - salvage - acc)
        acc += dep
        out.append((m, q(dep), q(cost - acc)))
    return out
