FUNCTIONS = {"VENDOR_MAINT": {"BP", "XK01", "XK02"}, "PAYMENT": {"F110", "F-53"}, "PO_CREATE": {"ME21N"}, "GR_POST": {"MIGO"},
             "INVOICE": {"MIRO"}, "PAY_RELEASE": {"F110"}}
RULES = [("VENDOR_MAINT", "PAYMENT", "HIGH"), ("PO_CREATE", "GR_POST", "MEDIUM"), ("PO_CREATE", "INVOICE", "HIGH")]
def conflicts(user_roles, role_tcodes, mitigations=()):
    out = []
    for user, roles in user_roles.items():
        tcodes = set().union(*(role_tcodes[r] for r in roles))
        funcs = {f for f, tc in FUNCTIONS.items() if tc & tcodes}
        for a, b, risk in RULES:
            if a in funcs and b in funcs:
                out.append({"user": user, "conflict": f"{a} x {b}", "risk": risk, "mitigated": (user, f"{a} x {b}") in mitigations})
    return out
