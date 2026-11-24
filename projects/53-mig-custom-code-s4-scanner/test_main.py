from main import scan
SRC = """REPORT zstock.
* SELECT * FROM mseg  (comment ignored)
SELECT * FROM mkpf INTO TABLE lt_head.
LOOP AT lt_head INTO ls_head.
  SELECT SINGLE * FROM konv INTO ls_konv WHERE knumv = ls_head-knumv.
ENDLOOP.
CALL TRANSACTION 'XD02' USING bdc.
"""
def test_findings():
    f = scan(SRC)
    lines = {(x["line"], x["severity"]) for x in f}
    assert (3, "HIGH") in lines and (5, "HIGH") in lines and (7, "HIGH") in lines
    assert not any(x["line"] == 2 for x in f)
    assert sum(1 for x in f if "inside loop" in x["fix"]) == 1
