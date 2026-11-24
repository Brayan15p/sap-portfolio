import random
class TokenBucket:
    def __init__(self, rate_per_s, burst):
        self.rate, self.cap, self.tokens, self.t = rate_per_s, burst, burst, 0.0
    def take(self, now):
        self.tokens = min(self.cap, self.tokens + (now - self.t) * self.rate); self.t = now
        if self.tokens >= 1: self.tokens -= 1; return 0.0
        return (1 - self.tokens) / self.rate
RETRYABLE = {429, 502, 503, 504}
def call_with_retry(send, max_attempts=5, base=0.5, seed=0):
    rnd = random.Random(seed); waits = []
    for attempt in range(1, max_attempts + 1):
        status, headers = send()
        if status < 400: return status, waits
        if status not in RETRYABLE or attempt == max_attempts: return status, waits
        wait = float(headers.get("Retry-After", base * 2 ** (attempt - 1) * (1 + rnd.random() * 0.1)))
        waits.append(round(wait, 3))
    return status, waits
