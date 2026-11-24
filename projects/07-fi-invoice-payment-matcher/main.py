def match(payments, invoices):
    open_inv = {i["id"]: dict(i) for i in invoices}
    out = []
    for p in payments:
        if p.get("ref") in open_inv:
            inv = open_inv[p["ref"]]
            kind = "EXACT_REF" if p["amount"] == inv["amount"] else "PARTIAL"
            inv["amount"] = round(inv["amount"] - p["amount"], 2)
            out.append({"payment": p["id"], "invoice": inv["id"], "type": kind})
            continue
        cands = [i for i in open_inv.values() if i["customer"] == p["customer"] and i["amount"] == p["amount"]]
        if len(cands) == 1:
            cands[0]["amount"] = 0
            out.append({"payment": p["id"], "invoice": cands[0]["id"], "type": "EXACT_AMOUNT"})
        else:
            out.append({"payment": p["id"], "invoice": None, "type": "REVIEW",
                        "reason": "ambiguous" if cands else "no candidate"})
    return out
