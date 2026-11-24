from decimal import Decimal, ROUND_HALF_UP
def q(x): return Decimal(x).quantize(Decimal("0.01"), ROUND_HALF_UP)
def compare(categories):
    out = {}
    for cat, c in categories.items():
        avail_cost = Decimal(c["opening_cost"]) + Decimal(c["purchases_cost"])
        avail_retail = Decimal(c["opening_retail"]) + Decimal(c["purchases_retail"]) - Decimal(c["markdowns"])
        ratio = avail_cost / avail_retail
        ending_retail = avail_retail - Decimal(c["sales_retail"])
        retail_method = q(ending_retail * ratio)
        out[cat] = {"cost_ratio": round(float(ratio), 4), "retail_method_value": retail_method,
                    "actual_cost_value": q(c["actual_ending_cost"]), "gap": q(retail_method - Decimal(c["actual_ending_cost"]))}
    return out
