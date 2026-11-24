from main import cpm
T = {"freeze": (2, []), "extract": (6, ["freeze"]), "load_master": (8, ["extract"]), "load_open_items": (10, ["load_master"]),
     "interfaces": (4, ["freeze"]), "reconcile": (4, ["load_open_items"]), "smoke_test": (3, ["reconcile", "interfaces"])}
def test_critical_path_and_window():
    r = cpm(T, 36)
    assert r["duration"] == 33 and r["fits_window"]
    assert r["critical_path"] == ["freeze", "extract", "load_master", "load_open_items", "reconcile", "smoke_test"]
    assert r["slack"]["interfaces"] == 24
