CHAIN = ["incomplete", "credit_block", "delivery_block", "not_confirmed", "not_picked", "not_billed"]
def classify(o):
    if o.get("missing_fields"): return "incomplete"
    if o.get("credit_status") == "B": return "credit_block"
    if o.get("delivery_block"): return "delivery_block"
    if o.get("confirmed_qty", 0) < o["qty"]: return "not_confirmed"
    if not o.get("picked"): return "not_picked"
    if not o.get("billed"): return "not_billed"
    return "done"
def monitor(orders):
    out = {k: {"count": 0, "value": 0} for k in CHAIN}
    for o in orders:
        k = classify(o)
        if k != "done": out[k]["count"] += 1; out[k]["value"] += o["value"]
    return dict(sorted(out.items(), key=lambda kv: -kv[1]["value"]))
