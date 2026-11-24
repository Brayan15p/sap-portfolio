def reconcile(shop: dict, b1: dict, tol=0.01):
    """each: {subtotal, discount, tax, total}"""
    if abs(shop["total"] - b1["total"]) <= tol:
        return {"status": "MATCH", "diff": 0, "causes": []}
    causes = []
    for k in ("subtotal", "discount", "tax"):
        d = round(shop[k] - b1[k], 2)
        if abs(d) > tol:
            causes.append({"component": k, "diff": d})
    explained = round(sum(c["diff"] * (-1 if c["component"] == "discount" else 1) for c in causes), 2)
    diff = round(shop["total"] - b1["total"], 2)
    residual = round(diff - explained, 2)
    if abs(residual) > tol:
        causes.append({"component": "rounding", "diff": residual})
    return {"status": "DIFF", "diff": diff, "causes": causes}
