from main import check
M = [{"material": "GUMMY1", "plant": "1000", "type": "FERT", "views": {"basic": {}, "sales": {"sales_org": "1000", "tax_class": "1"},
      "mrp": {"mrp_type": "PD", "lot_size": ""}, "accounting": {"valuation_class": "7920", "price": 1.2}}},
     {"material": "SUGAR", "plant": "1000", "type": "ROH", "views": {"basic": {}, "purchasing": {}, "mrp": {"mrp_type": "PD", "lot_size": "EX"}, "accounting": {"valuation_class": "3000", "price": 0.5}}}]
def test_missing_view_and_field():
    i = check(M)
    assert i == {("GUMMY1", "1000"): ["mrp.lot_size empty", "costing view missing"]}
