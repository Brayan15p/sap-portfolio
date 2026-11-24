def validate_entry(lines, expense_prefix="5"):
    errors = []
    if len({l["currency"] for l in lines}) > 1:
        errors.append("RULE_CURRENCY: entry mixes currencies")
    for n, l in enumerate(lines, 1):
        if (l.get("debit", 0) > 0) == (l.get("credit", 0) > 0):
            errors.append(f"Line {n} RULE_SIDE: exactly one of debit/credit must be > 0")
        if str(l["account"]).startswith(expense_prefix) and not l.get("cost_center"):
            errors.append(f"Line {n} RULE_COSTCENTER: expense account {l['account']} needs a cost center")
    bal = round(sum(l.get("debit", 0) - l.get("credit", 0) for l in lines), 2)
    if bal != 0:
        errors.append(f"RULE_BALANCE: debits - credits = {bal}")
    return errors
