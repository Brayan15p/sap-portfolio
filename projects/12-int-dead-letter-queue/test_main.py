from main import Pipeline

UNITS = {"UND": "EA"}
def mapping(m): return {"item": m["item"], "uom": UNITS[m["uom"]]}

def test_only_failed_message_is_reprocessed():
    p = Pipeline(mapping)
    for i, u in enumerate(["UND", "CAJA", "UND"]):
        p.handle({"corr": f"c{i}", "item": "A", "uom": u})
    assert list(p.dlq) == ["c1"] and "KeyError" in p.dlq["c1"]["error"]
    UNITS["CAJA"] = "BOX"
    p.reprocess()
    assert [d["corr"] for d in p.delivered] == ["c0", "c2", "c1"] and p.dlq == {}
