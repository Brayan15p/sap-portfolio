from decimal import Decimal, ROUND_HALF_UP
from datetime import date, timedelta

def cop(x): return Decimal(x).quantize(Decimal("1"), ROUND_HALF_UP)

def revalue(open_items, closing_rate, key_date: date):
    """open_items: [{id, kind: 'AP'|'AR', usd, booked_rate}]"""
    entries = []
    for i in open_items:
        booked = cop(Decimal(i["usd"]) * Decimal(i["booked_rate"]))
        now = cop(Decimal(i["usd"]) * Decimal(closing_rate))
        delta = now - booked
        if delta == 0: continue
        # AR: higher value = gain. AP: higher liability = loss.
        gain = delta if i["kind"] == "AR" else -delta
        acct = "Unrealized FX gain" if gain > 0 else "Unrealized FX loss"
        entries.append({"item": i["id"], "date": key_date, "account": acct, "amount": abs(gain)})
        entries.append({"item": i["id"], "date": key_date + timedelta(days=1), "account": acct, "amount": -abs(gain), "reversal": True})
    return entries
