import hashlib
from decimal import Decimal, ROUND_HALF_UP

WEIGHTS = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]

def nit_dv(nit: str) -> int:
    digits = [int(c) for c in nit if c.isdigit()][::-1]
    s = sum(d * WEIGHTS[i] for i, d in enumerate(digits)) % 11
    return s if s in (0, 1) else 11 - s

def m(x): return Decimal(x).quantize(Decimal("0.01"), ROUND_HALF_UP)

def cufe(num, date, time, subtotal, iva, inc, ica, total, nit_issuer, buyer_id, tech_key, env="2"):
    raw = (f"{num}{date}{time}{m(subtotal):.2f}01{m(iva):.2f}04{m(inc):.2f}03{m(ica):.2f}"
           f"{m(total):.2f}{nit_issuer}{buyer_id}{tech_key}{env}")
    return hashlib.sha384(raw.encode()).hexdigest()

def validate(inv):
    errors = []
    if nit_dv(inv["issuer_nit"]) != inv["issuer_dv"]:
        errors.append(f"Issuer DV should be {nit_dv(inv['issuer_nit'])}")
    sub = sum(m(Decimal(l["qty"]) * Decimal(l["price"])) for l in inv["lines"])
    by_rate = {}
    for l in inv["lines"]:
        base = m(Decimal(l["qty"]) * Decimal(l["price"]))
        by_rate[l["iva_rate"]] = by_rate.get(l["iva_rate"], 0) + base
    iva = sum(m(b * Decimal(r) / 100) for r, b in by_rate.items())
    total = sub + iva
    if m(inv["declared_total"]) != m(total):
        errors.append(f"Total {inv['declared_total']} != computed {total}")
    code = cufe(inv["number"], inv["date"], inv["time"], sub, iva, 0, 0, total,
                inv["issuer_nit"], inv["buyer_id"], inv["tech_key"])
    return {"errors": errors, "subtotal": sub, "iva_by_rate": by_rate, "iva": iva, "total": total, "cufe": code}
