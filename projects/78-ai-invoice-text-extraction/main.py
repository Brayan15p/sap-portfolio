import re
def money(s): return float(s.replace(".", "").replace(",", "."))
PAT = {"nit": r"NIT[:\s]*([\d\.]+-?\d)", "number": r"(?:FACTURA|No\.?)[^\n]*?([A-Z]{2,4}-?\d{3,})",
       "date": r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})", "subtotal": r"SUBTOTAL[:\s$]*([\d\.,]+)",
       "iva": r"IVA[^\n]*?\$\s*([\d\.,]+)\s*$", "total": r"TOTAL A PAGAR[:\s$]*([\d\.,]+)"}
def extract(text):
    out = {}
    for k, p in PAT.items():
        m = re.search(p, text, re.I | re.M); out[k] = m.group(1) if m else None
    for k in ("subtotal", "iva", "total"):
        if out[k]: out[k] = money(out[k])
    missing = [k for k, v in out.items() if v is None]
    ok = not missing and abs(out["subtotal"] + out["iva"] - out["total"]) < 1
    return {**out, "missing": missing, "route": "AUTO_POST" if ok else "REVIEW"}
