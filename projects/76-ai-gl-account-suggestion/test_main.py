from main import Suggester
TRAIN = [("servicio de aseo oficinas noviembre", "513505"), ("aseo y limpieza sede norte", "513505"),
         ("arriendo local comercial", "512010"), ("canon de arrendamiento bodega", "512010"),
         ("honorarios asesoria contable", "511025"), ("honorarios revisoria fiscal", "511025")]
def test_suggests_and_routes():
    s = Suggester().fit(TRAIN)
    assert s.predict("factura aseo oficinas diciembre")["account"] == "513505"
    assert s.predict("compra de flores")["route"] == "HUMAN"
