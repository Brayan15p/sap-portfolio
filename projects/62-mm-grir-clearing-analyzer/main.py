from datetime import date
def analyze(lines, today: date):
    out = []
    for l in lines:
        gr_v, ir_v = l["gr_qty"] * l["po_price"], l["ir_value"]
        diff = round(gr_v - ir_v, 2)
        if abs(diff) < 0.01: continue
        if l["ir_qty"] == 0: kind, action = "GR_NOT_INVOICED", "chase invoice / accrue"
        elif l["gr_qty"] == 0: kind, action = "INVOICED_NOT_RECEIVED", "post GR or block invoice"
        elif l["gr_qty"] == l["ir_qty"]: kind, action = "PRICE_DIFFERENCE", "credit memo or price variance posting"
        else: kind, action = "QUANTITY_DIFFERENCE", "match quantities"
        age = (today - l["last_movement"]).days
        out.append({"po": l["po"], "kind": kind, "diff": diff, "age_days": age, "action": action if age <= 90 else "write-off review (F.13 / MR11)"})
    return sorted(out, key=lambda x: -abs(x["diff"]))
