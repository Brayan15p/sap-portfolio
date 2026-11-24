def three_way_match(po_lines, gr, invoice_lines, price_tol_pct=2.0, qty_tol=0):
    """po_lines: {line: {qty, price}}, gr: {line: qty received}, invoice_lines: {line: {qty, price}}"""
    issues = []
    for line, inv in invoice_lines.items():
        po = po_lines.get(line)
        if po is None:
            issues.append(f"line {line}: not in purchase order"); continue
        received = gr.get(line, 0)
        if inv["qty"] > received + qty_tol:
            issues.append(f"line {line}: invoiced {inv['qty']} > received {received}")
        diff_pct = (inv["price"] - po["price"]) / po["price"] * 100
        if diff_pct > price_tol_pct:
            issues.append(f"line {line}: price {inv['price']} is {diff_pct:.1f}% above PO {po['price']}")
    return {"payment_block": bool(issues), "issues": issues}
