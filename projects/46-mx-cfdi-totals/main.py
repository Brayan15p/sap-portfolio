import re
from decimal import Decimal, ROUND_HALF_UP

RFC = re.compile(r"^([A-ZÑ&]{3,4})(\d{2})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([A-Z\d]{3})$")

def q(x): return Decimal(x).quantize(Decimal("0.01"), ROUND_HALF_UP)

def rfc_valid(rfc: str) -> str | None:
    m = RFC.match(rfc.upper())
    if not m: return None
    return "PERSONA_MORAL" if len(m.group(1)) == 3 else "PERSONA_FISICA"

def cfdi_totals(lines, issuer_rfc, receiver_rfc, iva_rate="0.16"):
    t_issuer, t_receiver = rfc_valid(issuer_rfc), rfc_valid(receiver_rfc)
    if not t_issuer or not t_receiver: raise ValueError("Invalid RFC")
    sub = sum(q(Decimal(l["qty"]) * Decimal(l["unit"])) for l in lines)
    disc = sum(q(l.get("discount", 0)) for l in lines)
    base = sub - disc
    iva = q(base * Decimal(iva_rate))
    withheld_iva = withheld_isr = Decimal(0)
    if t_issuer == "PERSONA_FISICA" and t_receiver == "PERSONA_MORAL":   # professional services
        withheld_iva = q(iva * 2 / 3); withheld_isr = q(base * Decimal("0.10"))
    total = base + iva - withheld_iva - withheld_isr
    return {"SubTotal": sub, "Descuento": disc, "TotalImpuestosTrasladados": iva,
            "TotalImpuestosRetenidos": withheld_iva + withheld_isr, "Total": total}
