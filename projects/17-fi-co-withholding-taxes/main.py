from decimal import Decimal, ROUND_HALF_UP

def r(x): return Decimal(x).quantize(Decimal("1"), ROUND_HALF_UP)

# Illustrative parameters; real values change every year by decree and must come from configuration.
CONCEPTS = {
    "SERVICIOS":  {"rate": Decimal("0.04"),  "min_uvt": Decimal("4")},
    "COMPRAS":    {"rate": Decimal("0.025"), "min_uvt": Decimal("27")},
    "HONORARIOS": {"rate": Decimal("0.11"),  "min_uvt": Decimal("0")},
}

def withholdings(base, iva, concept, uvt, ica_per_mil, vendor_is_iva_responsible=True, reteiva_share=Decimal("0.15")):
    base, iva = Decimal(base), Decimal(iva)
    c = CONCEPTS[concept]
    rete = r(base * c["rate"]) if base >= c["min_uvt"] * Decimal(uvt) else Decimal(0)
    reteiva = r(iva * reteiva_share) if vendor_is_iva_responsible and iva > 0 else Decimal(0)
    reteica = r(base * Decimal(ica_per_mil) / 1000)
    total = base + iva
    net = total - rete - reteiva - reteica
    lines = [("Expense", base, 0), ("IVA descontable", iva, 0),
             ("Retefuente por pagar", 0, rete), ("ReteIVA por pagar", 0, reteiva),
             ("ReteICA por pagar", 0, reteica), ("Proveedor", 0, net)]
    assert sum(l[1] for l in lines) == sum(l[2] for l in lines), "entry must balance"
    return {"retefuente": rete, "reteiva": reteiva, "reteica": reteica, "net_payable": net, "lines": lines}
