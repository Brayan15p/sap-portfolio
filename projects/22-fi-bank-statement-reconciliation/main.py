import re

def reconcile(statement, open_items, fee_words=("COMISION", "GMF", "4X1000", "IVA COMISION")):
    posted, worklist = [], []
    open_by_ref = {i["ref"]: i for i in open_items}
    for line in statement:
        text = line["text"].upper()
        if line["amount"] < 0 and any(w in text for w in fee_words):
            posted.append({"line": line["id"], "account": "Bank charges", "amount": -line["amount"]}); continue
        ref = next((r for r in re.findall(r"[A-Z]{2,3}-?\d+", text) if r.replace("-", "") in {k.replace("-", "") for k in open_by_ref}), None)
        if ref:
            inv = next(v for k, v in open_by_ref.items() if k.replace("-", "") == ref.replace("-", ""))
            status = "CLEARED" if line["amount"] == inv["amount"] else "PARTIAL"
            posted.append({"line": line["id"], "invoice": inv["ref"], "status": status}); continue
        same = [i for i in open_items if i["amount"] == line["amount"]]
        if len(same) == 1:
            posted.append({"line": line["id"], "invoice": same[0]["ref"], "status": "CLEARED_BY_AMOUNT"})
        else:
            worklist.append({"line": line["id"], "reason": "ambiguous amount" if same else "no match"})
    return posted, worklist
