from datetime import datetime as D
from main import review
def test_findings():
    s = [{"id": "FF1", "ticket": "", "start": D(2026, 11, 1, 8), "end": D(2026, 11, 1, 14), "tcodes": ["SE16N", "FB03"], "reviewed_at": None},
         {"id": "FF2", "ticket": "INC1", "start": D(2026, 11, 2, 8), "end": D(2026, 11, 2, 9), "tcodes": ["FB03"], "reviewed_at": D(2026, 11, 2, 12)}]
    r = review(s)
    assert r == [{"session": "FF1", "issues": ["no ticket", "exceeded duration", "critical tcodes ['SE16N']", "review late or missing"]}]
