from datetime import date

def pick(batches, qty, today: date, min_days_left=30):
    eligible = sorted((b for b in batches
                       if b["status"] == "UNRESTRICTED" and (b["expiry"] - today).days >= min_days_left and b["qty"] > 0),
                      key=lambda b: (b["expiry"], b["batch"]))
    picks, need = [], qty
    for b in eligible:
        take = min(b["qty"], need)
        picks.append((b["batch"], take)); need -= take
        if need == 0: break
    if need:
        raise ValueError(f"Short by {need}: only {qty - need} available under FEFO rules")
    return picks
