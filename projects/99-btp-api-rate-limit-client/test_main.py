from main import TokenBucket, call_with_retry
def test_bucket_limits_rate():
    b = TokenBucket(rate_per_s=2, burst=2)
    assert b.take(0) == 0 and b.take(0) == 0 and b.take(0) > 0 and b.take(1.0) == 0
def test_retry_honors_retry_after_and_stops_on_400():
    seq = iter([(429, {"Retry-After": "3"}), (503, {}), (200, {})])
    status, waits = call_with_retry(lambda: next(seq))
    assert status == 200 and waits[0] == 3.0 and 1.0 <= waits[1] <= 1.1
    assert call_with_retry(lambda: (400, {}))[1] == []
