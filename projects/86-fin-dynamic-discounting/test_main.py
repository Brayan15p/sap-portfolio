from main import apr, select
def test_classic_2_10_net_30():
    assert apr(2, 20) == 37.24
def test_selection_beats_hurdle_within_cash():
    inv = [{"id": "A", "amount": 1_000_000, "days_early": 30}, {"id": "B", "amount": 1_000_000, "days_early": 5}]
    chosen, saving = select(inv, cash=1_500_000, hurdle_apr=15)
    assert [c["id"] for c in chosen] == ["A"] and saving == 20000.0
