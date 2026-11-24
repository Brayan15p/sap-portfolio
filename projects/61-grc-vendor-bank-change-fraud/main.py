from datetime import date
def alerts(changes, payments, days=15):
    out = []
    for p in payments:
        for c in changes:
            if c["vendor"] == p["vendor"] and c["new_account"] == p["account"] and 0 <= (p["date"] - c["date"]).days <= days:
                out.append({"payment": p["id"], "reason": f"paid {(p['date'] - c['date']).days} days after bank change"})
                if c["user"] == p["released_by"]: out.append({"payment": p["id"], "reason": "same user changed bank and released payment"})
    acc = {}
    for c in changes: acc.setdefault(c["new_account"], set()).add(c["vendor"])
    for a, vs in acc.items():
        if len(vs) > 1: out.append({"account": a, "reason": f"shared by vendors {sorted(vs)}"})
    return out
