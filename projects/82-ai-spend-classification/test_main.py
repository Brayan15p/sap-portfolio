from main import classify, cube
def test_classification_and_cube():
    assert classify("Caja guantes quirurgicos talla M") == "42 Medical" and classify("Resma papel carta") == "44 Office"
    c = cube([{"text": "licencia software antivirus", "amount": 1000}, {"text": "servicio raro", "amount": 50}])
    assert c == {"43 IT": 1000, "UNCLASSIFIED": 50}
