from main import analyze

LOG = """
2026-11-23 08:01 JPEREZ CX_SY_ZERODIVIDE ZSD_MARGIN ZSD_MARGIN_F01 120
2026-11-23 08:05 MLOPEZ CX_SY_ZERODIVIDE ZSD_MARGIN ZSD_MARGIN_F01 120
2026-11-23 09:00 JPEREZ CX_SY_ZERODIVIDE ZSD_MARGIN ZSD_MARGIN_F01 120
2026-11-23 09:10 BATCH TSV_TNEW_PAGE_ALLOC_FAILED ZFI_EXTRACT ZFI_EXTRACT 88
garbage line
"""

def test_top_offender_with_users_and_hint():
    r = analyze(LOG)
    t = r["top"][0]
    assert (t["exception"], t["count"], t["users"]) == ("CX_SY_ZERODIVIDE", 3, 2)
    assert "zero quantities" in t["hint"] and r["unparsed"] == 1
