from decimal import Decimal
from main import translate, eliminate

TB = {"Cash": ("assets", 1000), "Payables": ("liabilities", 400), "Capital": ("equity", 500),
      "Sales": ("revenue", 300), "Costs": ("expense", 200)}

def test_balance_sheet_balances_with_cta():
    out, ni = translate(TB, closing="220", average="210", historical_equity={"Capital": 100000})
    assets = sum(v for t, v in out.values() if t == "assets")
    le = sum(v for t, v in out.values() if t in ("liabilities", "equity"))
    assert ni == 21000 and assets == le + ni and out["CTA"][1] == 11000

def test_intercompany_mismatch_reported():
    _, issues = eliminate([{"pair": "CO-MX", "receivable": 50000, "payable": 50000},
                           {"pair": "CO-US", "receivable": 80000, "payable": 70000}])
    assert issues == ["CO-US: IC difference 10000"]
