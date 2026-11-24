from datetime import date

BUCKETS = [(0, 30, "0-30"), (31, 60, "31-60"), (61, 90, "61-90"), (91, 10**6, "90+")]

def aging(invoices, payments, as_of: date):
    """invoices: [{id, customer, due, amount}], payments: [{invoice_id, amount}]"""
    paid = {}
    for p in payments:
        paid[p["invoice_id"]] = paid.get(p["invoice_id"], 0) + p["amount"]
    report = {}
    for inv in invoices:
        open_amt = round(inv["amount"] - paid.get(inv["id"], 0), 2)
        if open_amt <= 0:
            continue
        days = (as_of - inv["due"]).days
        bucket = "not due" if days < 0 else next(b for lo, hi, b in BUCKETS if lo <= days <= hi)
        cust = report.setdefault(inv["customer"], {})
        cust[bucket] = round(cust.get(bucket, 0) + open_amt, 2)
    return report
