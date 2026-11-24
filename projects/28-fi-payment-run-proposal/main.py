from datetime import date

def proposal(items, run_date: date, next_run: date, bank_limit, blocked_vendors=()):
    cands, exceptions = [], []
    for i in items:
        if i["vendor"] in blocked_vendors or i.get("block"):
            exceptions.append((i["id"], "blocked")); continue
        disc_ok = i.get("disc_date") and run_date <= i["disc_date"]
        pay_now = disc_ok or i["due"] < next_run
        if not pay_now:
            continue
        disc = round(i["amount"] * i.get("disc_pct", 0) / 100) if disc_ok else 0
        cands.append({"id": i["id"], "pay": i["amount"] - disc, "saving": disc, "due": i["due"]})
    cands.sort(key=lambda c: (-c["saving"], c["due"]))
    paid, total = [], 0
    for c in cands:
        if total + c["pay"] <= bank_limit:
            paid.append(c); total += c["pay"]
        else:
            exceptions.append((c["id"], "bank limit"))
    return paid, exceptions, total
