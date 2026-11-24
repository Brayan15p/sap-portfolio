TIERS = [(0, 0.0), (500_000_000, 2.0), (1_000_000_000, 3.0)]

def rate_for(cum):
    return max(r for t, r in TIERS if cum >= t)

def accruals(monthly_sales):
    cum, accrued, rows = 0, 0, []
    for month, sales in enumerate(monthly_sales, 1):
        cum += sales
        should = round(cum * rate_for(cum) / 100)
        delta = should - accrued
        rows.append({"month": month, "cum_sales": cum, "rate": rate_for(cum), "accrual": delta, "catch_up": delta > round(sales * rate_for(cum) / 100)})
        accrued = should
    return rows, accrued
