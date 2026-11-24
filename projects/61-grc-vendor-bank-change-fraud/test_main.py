from datetime import date
from main import alerts
def test_three_red_flags():
    ch = [{"vendor": "V1", "new_account": "123", "date": date(2026, 11, 1), "user": "pepe"}, {"vendor": "V2", "new_account": "123", "date": date(2026, 9, 1), "user": "ana"}]
    pay = [{"id": "P1", "vendor": "V1", "account": "123", "date": date(2026, 11, 5), "released_by": "pepe"}]
    reasons = [a["reason"] for a in alerts(ch, pay)]
    assert "paid 4 days after bank change" in reasons and "same user changed bank and released payment" in reasons
    assert "shared by vendors ['V1', 'V2']" in reasons
