CH = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def gstin_checksum(g14: str) -> str:
    f, s = 2, 0
    for c in reversed(g14):
        a = f * CH.index(c); f = 1 if f == 2 else 2; s += a // 36 + a % 36
    return CH[(36 - s % 36) % 36]

def gstin_valid(g: str) -> bool:
    g = g.upper()
    return len(g) == 15 and g[:2].isdigit() and g[13] == "Z" and gstin_checksum(g[:14]) == g[14]

def gst(supplier_gstin, customer_gstin, taxable, rate):
    for x in (supplier_gstin, customer_gstin):
        if not gstin_valid(x): raise ValueError(f"Invalid GSTIN {x}")
    tax = round(taxable * rate / 100, 2)
    if supplier_gstin[:2] == customer_gstin[:2]:
        return {"CGST": round(tax / 2, 2), "SGST": round(tax / 2, 2), "IGST": 0.0, "total": taxable + tax}
    return {"CGST": 0.0, "SGST": 0.0, "IGST": tax, "total": taxable + tax}
