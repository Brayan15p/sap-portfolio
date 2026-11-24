import random
SIZES = {"annual": 1, "quarterly": 2, "monthly": 2, "weekly": 5, "daily": 25, "multiple_daily": 40}
def sample(population, frequency, seed, key_threshold=None):
    n = SIZES[frequency]
    forced = [p for p in population if key_threshold is not None and p["amount"] >= key_threshold]
    rest = [p for p in population if p not in forced]
    rnd = random.Random(seed).sample(rest, max(0, min(len(rest), n - len(forced))))
    return forced + rnd
def evaluate(results, tolerated=0):
    exc = sum(1 for r in results if not r["passed"])
    return "EFFECTIVE" if exc <= tolerated else "DEFICIENCY"
