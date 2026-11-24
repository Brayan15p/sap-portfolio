from decimal import Decimal, ROUND_HALF_UP

def money(x): return Decimal(x).quantize(Decimal("0.01"), ROUND_HALF_UP)

def price(item, qty, customer, records):
    # Access sequence for base price PR00: most specific record wins
    for key in [("cust_mat", customer, item), ("pricelist", records["customer_pricelist"].get(customer), item), ("mat", item)]:
        if key in records["PR00"]:
            base = Decimal(records["PR00"][key]); source = key[0]; break
    else:
        raise LookupError(f"No PR00 for {item}")
    steps = [("PR00 base price", source, money(base * qty))]
    net = base * qty
    disc = Decimal(records["K007"].get(customer, 0))
    if disc:
        v = -net * disc / 100; net += v; steps.append(("K007 customer discount", f"{disc}%", money(v)))
    scale = max([s for s in records["scales"].get(item, []) if qty >= s[0]], default=None)
    if scale:
        v = -net * Decimal(scale[1]) / 100; net += v; steps.append(("VA00 volume scale", f">={scale[0]}: {scale[1]}%", money(v)))
    tax = net * Decimal(records["MWST"]) / 100
    steps.append(("Net value", "", money(net))); steps.append(("MWST IVA", f"{records['MWST']}%", money(tax)))
    steps.append(("Total", "", money(net + tax)))
    return steps
