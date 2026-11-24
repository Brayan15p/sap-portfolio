from main import parse, run
R = [{"id": 1, "status": "OVERDUE", "amount": 8e6, "city": "MED"}, {"id": 2, "status": "OVERDUE", "amount": 2e6, "city": "MED"},
     {"id": 3, "status": "PAID", "amount": 9e6, "city": "MED"}, {"id": 4, "status": "OVERDUE", "amount": 9e6, "city": "BOG"}]
def test_spanish_question_to_filters():
    f, rows = run("Facturas vencidas de más de 5 millones en Medellín", R)
    assert f == {"status": "OVERDUE", "min_amount": 5e6, "city": "MED"} and [r["id"] for r in rows] == [1]
