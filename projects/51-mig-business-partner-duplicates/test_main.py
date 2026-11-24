from main import clusters
R = [{"id": "C1", "name": "Distribuidora El Sol S.A.S.", "city": "BOG", "tax_id": "900123456", "last_activity": "2026-10"},
     {"id": "V7", "name": "DISTRIBUIDORA EL SOL SAS", "city": "BOG", "tax_id": "", "last_activity": "2025-01"},
     {"id": "C2", "name": "Ferretería Andina", "city": "MED", "tax_id": "800999111"},
     {"id": "C3", "name": "Ferreteria Andina Ltda", "city": "MED", "tax_id": "800999111"},
     {"id": "C4", "name": "Ferreteria Andina", "city": "CAL", "tax_id": ""}]
def test_clusters_by_tax_and_fuzzy_name_not_across_cities():
    c = sorted(clusters(R), key=lambda x: x["survivor"])
    assert {"survivor": "C1", "merge": ["V7"]} in c
    assert any(set(x["merge"] + [x["survivor"]]) == {"C2", "C3"} for x in c)
    assert all("C4" not in x["merge"] and x["survivor"] != "C4" for x in c)
