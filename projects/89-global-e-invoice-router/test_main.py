from main import route
def test_routes_and_blocks():
    assert route({"country": "MX", "rfc_receptor": "XAXX010101000", "uso_cfdi": "G03"})["channel"] == "PAC"
    r = route({"country": "BR", "cfop": "5102"})
    assert r["status"] == "BLOCKED" and r["missing"] == ["access_key"]
    assert route({"country": "CL"})["status"] == "PDF_EMAIL"
