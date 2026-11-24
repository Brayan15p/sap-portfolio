from main import match

INV = [{"id": "F1", "customer": "C1", "amount": 500}, {"id": "F2", "customer": "C1", "amount": 500},
       {"id": "F3", "customer": "C2", "amount": 800}]

def test_two_invoices_same_amount_without_ref_go_to_review():
    r = match([{"id": "P1", "customer": "C1", "amount": 500}], INV)
    assert r[0]["type"] == "REVIEW" and r[0]["reason"] == "ambiguous"

def test_exact_by_ref_and_partial():
    r = match([{"id": "P1", "customer": "C1", "amount": 500, "ref": "F2"},
               {"id": "P2", "customer": "C2", "amount": 300, "ref": "F3"}], INV)
    assert [x["type"] for x in r] == ["EXACT_REF", "PARTIAL"]

def test_unique_amount_matches():
    assert match([{"id": "P1", "customer": "C2", "amount": 800}], INV)[0]["invoice"] == "F3"
