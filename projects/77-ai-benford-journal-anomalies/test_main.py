import random
from main import analyze
def test_natural_vs_manipulated():
    rnd = random.Random(1)
    natural = [{"user": "ok", "amount": round(10 ** rnd.uniform(2, 7), 2)} for _ in range(2000)]
    fraud = [{"user": "bad", "amount": rnd.choice([9_800_000, 9_900_000, 9_700_000, 8_500_000])} for _ in range(200)]
    r = analyze(natural + fraud, approval_limit=10_000_000)
    assert not r["ok"]["flag"] and r["bad"]["flag"] and r["bad"]["just_below_limit"] > 2
