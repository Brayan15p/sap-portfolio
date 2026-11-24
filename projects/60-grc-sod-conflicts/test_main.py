from main import conflicts
ROLES = {"Z_AP_CLERK": {"MIRO", "XK02"}, "Z_TREASURY": {"F110"}, "Z_BUYER": {"ME21N"}, "Z_WH": {"MIGO"}}
def test_conflicts_and_mitigation():
    c = conflicts({"ana": ["Z_AP_CLERK", "Z_TREASURY"], "luis": ["Z_BUYER", "Z_WH"], "eva": ["Z_BUYER"]}, ROLES,
                  mitigations={("luis", "PO_CREATE x GR_POST")})
    assert {"user": "ana", "conflict": "VENDOR_MAINT x PAYMENT", "risk": "HIGH", "mitigated": False} in c
    assert {"user": "luis", "conflict": "PO_CREATE x GR_POST", "risk": "MEDIUM", "mitigated": True} in c
    assert not any(x["user"] == "eva" for x in c)
