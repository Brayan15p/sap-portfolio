import pytest
from main import sync, make_source

ITEMS = [{"code": f"A{i}", "updated": "2026-11-0" + str(1 + i % 3)} for i in range(7)]

def test_resume_after_cut_no_loss_no_dupes():
    applied, cp = [], {}
    src = make_source(ITEMS)
    with pytest.raises(ConnectionError):
        sync(src, cp, applied.append, fail_after_pages=2)
    sync(src, cp, applied.append)
    assert sorted(i["code"] for i in applied) == sorted(i["code"] for i in ITEMS)
    assert len(applied) == len(ITEMS)

def test_second_run_only_changes():
    applied, cp = [], {}
    sync(make_source(ITEMS), cp, applied.append)
    changed = ITEMS + [{"code": "A0", "updated": "2026-11-09"}]
    new = []
    sync(make_source(changed), cp, new.append)
    assert [i["code"] for i in new] == ["A0"]
