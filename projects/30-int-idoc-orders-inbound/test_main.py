from main import Inbound

IDOC = """
E1EDK01|CURCY=COP|BSART=ZOR
E1EDKA1|PARVW=AG|PARTN=EXITO-001
E1EDP01|POSEX=10|MENGE=24|IDTNR=7701234567890
E1EDP01|POSEX=20|MENGE=12|IDTNR=7709999999999
"""

def test_51_then_53_after_master_data_fix():
    mm = {"7701234567890": "A1001"}
    ib = Inbound({"EXITO-001": "C0001"}, mm)
    assert ib.process("0000001", IDOC) == 51
    assert ib.status["0000001"][1] == ["Item 20: no material for 7709999999999"]
    mm["7709999999999"] = "A2002"
    assert ib.process("0000001", IDOC) == 53
