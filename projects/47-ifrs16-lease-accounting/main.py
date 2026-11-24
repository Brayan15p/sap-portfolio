from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 28

def q(x): return Decimal(x).quantize(Decimal("0.01"), ROUND_HALF_UP)

def lease_schedule(payment, months, annual_rate, initial_direct_costs=0, in_advance=False):
    i = Decimal(annual_rate) / 12 / 100; pay = Decimal(payment)
    pv = sum(pay / (1 + i) ** (t if not in_advance else t - 1) for t in range(1, months + 1))
    liability = q(pv); rou = q(pv + Decimal(initial_direct_costs))
    dep = q(rou / months); rows = []; bal = liability
    for t in range(1, months + 1):
        if in_advance:
            principal = pay; bal -= principal; interest = q(bal * i); bal += interest
        else:
            interest = q(bal * i); principal = pay - interest; bal -= principal
        if t == months: bal = q(0)
        rows.append({"month": t, "interest": q(interest), "principal": q(principal), "liability": q(bal), "rou_depreciation": dep})
    return {"initial_liability": liability, "initial_rou": rou, "rows": rows}
