from main import extract
TXT = """DISTRIBUIDORA ANDINA SAS NIT: 900.123.456-7
FACTURA ELECTRONICA DE VENTA FE-10234
Fecha: 2026-11-20
SUBTOTAL $ 1.000.000,00
IVA 19% $ 190.000,00
TOTAL A PAGAR $ 1.190.000,00"""
def test_extract_and_validate():
    r = extract(TXT)
    assert r["nit"] == "900.123.456-7" and r["number"] == "FE-10234" and r["total"] == 1190000.0 and r["route"] == "AUTO_POST"
    assert extract(TXT.replace("1.190.000", "1.290.000"))["route"] == "REVIEW"
