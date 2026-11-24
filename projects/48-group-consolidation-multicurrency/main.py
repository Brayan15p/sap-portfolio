from decimal import Decimal, ROUND_HALF_UP

def q(x): return Decimal(x).quantize(Decimal("1"), ROUND_HALF_UP)

def translate(tb, closing, average, historical_equity):
    """tb: {account: (type, amount)} type in assets, liabilities, equity, revenue, expense"""
    out, net_income = {}, Decimal(0)
    for acc, (typ, amt) in tb.items():
        amt = Decimal(amt)
        if typ in ("assets", "liabilities"): v = q(amt * Decimal(closing))
        elif typ == "equity": v = q(Decimal(historical_equity[acc]))
        else:
            v = q(amt * Decimal(average)); net_income += v if typ == "revenue" else -v
        out[acc] = (typ, v)
    a = sum(v for t, v in out.values() if t == "assets")
    le = sum(v for t, v in out.values() if t in ("liabilities", "equity"))
    out["CTA"] = ("equity", a - le - net_income)
    return out, net_income

def eliminate(ic_pairs, tol=Decimal(1000)):
    issues, entries = [], []
    for p in ic_pairs:
        diff = Decimal(p["receivable"]) - Decimal(p["payable"])
        if abs(diff) > tol: issues.append(f"{p['pair']}: IC difference {diff}")
        entries.append((p["pair"], -Decimal(p["receivable"]), Decimal(p["payable"])))
    return entries, issues
