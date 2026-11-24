from main import schedule
J = {"MRP": (120, []), "BILLING": (60, []), "PAYRUN": (30, ["BILLING"]), "BI_EXTRACT": (90, ["MRP", "BILLING"])}
def test_dependencies_and_deadline():
    plan, end, late = schedule(J, slots=2, deadline=200)
    starts = {j: s for j, s, _ in plan}
    assert starts["BI_EXTRACT"] >= 120 and starts["PAYRUN"] >= 60
    assert end == 210 and late == ["BI_EXTRACT"]
