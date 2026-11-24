import math, re
from collections import Counter, defaultdict
def tokens(t): return re.findall(r"[a-záéíóúñ]{3,}", t.lower())
class Suggester:
    def fit(self, rows):
        self.prior = Counter(a for _, a in rows); self.words = defaultdict(Counter); self.vocab = set()
        for text, acc in rows:
            for w in tokens(text): self.words[acc][w] += 1; self.vocab.add(w)
        return self
    def predict(self, text, min_conf=0.6):
        scores = {}
        for acc, n in self.prior.items():
            total = sum(self.words[acc].values()); s = math.log(n / sum(self.prior.values()))
            for w in tokens(text): s += math.log((self.words[acc][w] + 1) / (total + len(self.vocab)))
            scores[acc] = s
        m = max(scores.values()); probs = {a: math.exp(s - m) for a, s in scores.items()}; z = sum(probs.values())
        best = max(probs, key=probs.get); conf = probs[best] / z
        return {"account": best if conf >= min_conf else None, "confidence": round(conf, 2), "route": "AUTO" if conf >= min_conf else "HUMAN"}
