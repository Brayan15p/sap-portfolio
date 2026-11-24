from main import footprint
L = [{"supplier": "TransAndes", "category": "Transport", "amount": 200_000_000}, {"supplier": "TransAndes", "activity": "diesel_l", "qty": 10_000},
     {"supplier": "EmpaquesSA", "category": "Packaging", "amount": 50_000_000}, {"supplier": "SoftCo", "category": "IT", "amount": 20_000_000}]
def test_hotspots():
    r = footprint(L)
    assert r["hotspots_80pct"] == ["TransAndes", "EmpaquesSA"] and r["by_supplier_t"]["TransAndes"] == 116.8
