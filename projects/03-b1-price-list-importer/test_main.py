from main import validate

H = "item,uom,currency,price,valid_from,valid_to\n"
ARGS = ({"A1"}, {"UND"}, {"COP", "USD"})

def test_valid_file_applies():
    r = validate(H + "A1,UND,COP,1000,2026-12-01,2026-12-31\n", *ARGS)
    assert len(r["apply"]) == 1 and r["errors"] == []

def test_invalid_row_blocks_whole_file_with_row_number():
    r = validate(H + "A1,UND,COP,1000,2026-12-01,2026-12-31\nA1,KG,EUR,x,2026-12-31,2026-12-01\n", *ARGS)
    assert r["apply"] == []
    assert r["errors"][0]["row"] == 3 and len(r["errors"][0]["errors"]) == 4
