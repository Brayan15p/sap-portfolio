from main import analyze
T = ["  12.0ms 5000 SELECT * FROM MARA"] + [f"   0.8ms 1 SELECT NAME1 FROM KNA1 WHERE KUNNR = '{i:010d}'" for i in range(200)]
def test_detects_n_plus_one_and_full_scan():
    f, s = analyze(T)
    kinds = [x[0] for x in f]
    assert "IDENTICAL_REPEATED" in kinds and "NO_WHERE" in kinds
    rep = next(x for x in f if x[0] == "IDENTICAL_REPEATED")
    assert rep[2]["exec"] == 200 and round(rep[2]["ms"], 1) == 160.0
