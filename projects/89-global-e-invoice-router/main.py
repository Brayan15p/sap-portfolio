RULES = {"CO": {"format": "UBL 2.1 (DIAN)", "channel": "Technology provider -> DIAN", "model": "clearance", "required": ["cufe", "buyer_tax_id"]},
         "MX": {"format": "CFDI 4.0", "channel": "PAC", "model": "clearance", "required": ["rfc_receptor", "uso_cfdi"]},
         "BR": {"format": "NF-e XML", "channel": "SEFAZ", "model": "clearance", "required": ["access_key", "cfop"]},
         "IN": {"format": "e-invoice JSON (IRN)", "channel": "IRP", "model": "clearance", "required": ["gstin_buyer", "hsn"]},
         "DE": {"format": "XRechnung / Peppol BIS", "channel": "Peppol", "model": "post-audit", "required": ["buyer_reference"]},
         "IT": {"format": "FatturaPA", "channel": "SDI", "model": "clearance", "required": ["codice_destinatario"]}}
def route(invoice):
    r = RULES.get(invoice["country"])
    if not r: return {"status": "PDF_EMAIL", "missing": []}
    missing = [f for f in r["required"] if not invoice.get(f)]
    return {"status": "BLOCKED" if missing else "READY", "missing": missing, **{k: r[k] for k in ("format", "channel", "model")}}
