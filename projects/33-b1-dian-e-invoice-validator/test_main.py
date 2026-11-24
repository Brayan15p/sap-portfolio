from decimal import Decimal
from main import nit_dv, validate

def test_nit_check_digit_known_values():
    assert nit_dv("800197268") == 4     # DIAN NIT 800.197.268-4
    assert nit_dv("860034313") == 7
    assert nit_dv("900373115") == 3

INV = {"issuer_nit": "800197268", "issuer_dv": 4, "buyer_id": "1020304050", "number": "SETP990000001",
       "date": "2026-11-23", "time": "10:00:00-05:00", "tech_key": "fc8eac422eba16e22ffd8c6f94b3f40a6e38162c",
       "lines": [{"qty": 2, "price": "100000", "iva_rate": 19}, {"qty": 1, "price": "50000", "iva_rate": 5}, {"qty": 3, "price": "10000", "iva_rate": 0}],
       "declared_total": "320500"}

def test_taxes_by_rate_and_total():
    r = validate(INV)
    assert r["iva"] == Decimal("40500.00") and r["errors"] == []

def test_cufe_is_deterministic_sha384_and_changes_with_total():
    a = validate(INV)["cufe"]; assert len(a) == 96 and a == validate(INV)["cufe"]
    b = validate({**INV, "lines": INV["lines"][:2], "declared_total": "290500"})["cufe"]
    assert a != b

def test_wrong_dv_and_total_rejected():
    r = validate({**INV, "issuer_dv": 1, "declared_total": "1"})
    assert len(r["errors"]) == 2
