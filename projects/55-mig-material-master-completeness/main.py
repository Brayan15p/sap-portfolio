REQUIRED = {"FERT": ["basic", "sales", "mrp", "accounting", "costing"],
            "ROH": ["basic", "purchasing", "mrp", "accounting"],
            "HAWA": ["basic", "purchasing", "sales", "accounting"]}
FIELDS = {"mrp": ["mrp_type", "lot_size"], "accounting": ["valuation_class", "price"], "sales": ["sales_org", "tax_class"]}
def check(materials):
    issues = {}
    for m in materials:
        miss = []
        for view in REQUIRED.get(m["type"], ["basic"]):
            v = m.get("views", {}).get(view)
            if v is None: miss.append(f"{view} view missing"); continue
            for f in FIELDS.get(view, []):
                if not v.get(f): miss.append(f"{view}.{f} empty")
        if miss: issues[(m["material"], m["plant"])] = miss
    return issues
