from main import sample, evaluate
POP = [{"id": i, "amount": i * 10} for i in range(1, 501)]
def test_reproducible_with_forced_key_items():
    a = sample(POP, "daily", seed=42, key_threshold=4980); b = sample(POP, "daily", seed=42, key_threshold=4980)
    assert a == b and len(a) == 25 and {499, 500} <= {x["id"] for x in a}
def test_evaluation():
    assert evaluate([{"passed": True}] * 24 + [{"passed": False}]) == "DEFICIENCY"
