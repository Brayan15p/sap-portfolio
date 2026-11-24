from main import validate_entry

def L(acc, d=0, c=0, cc=None, cur="COP"):
    return {"account": acc, "debit": d, "credit": c, "cost_center": cc, "currency": cur}

def test_valid():
    assert validate_entry([L("510505", d=100, cc="CC1"), L("220505", c=100)]) == []

def test_unbalanced_and_missing_cost_center():
    e = validate_entry([L("510505", d=100), L("220505", c=90)])
    assert "Line 1 RULE_COSTCENTER: expense account 510505 needs a cost center" in e
    assert "RULE_BALANCE: debits - credits = 10" in e

def test_mixed_currency():
    assert "RULE_CURRENCY: entry mixes currencies" in validate_entry([L("1", d=1), L("2", c=1, cur="USD")])
