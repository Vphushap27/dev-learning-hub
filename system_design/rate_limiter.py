"""Token Bucket Rate Limiter - API gateways mein common."""
import time


class TokenBucket:
    def __init__(self, capacity, refill_per_sec, clock=time.monotonic):
        self.capacity = capacity
        self.refill = refill_per_sec
        self.tokens = float(capacity)
        self.clock = clock
        self.last = clock()

    def allow(self, cost=1):
        now = self.clock()
        self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.refill)
        self.last = now
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False


def demo():
    tb = TokenBucket(capacity=3, refill_per_sec=1)
    print("Burst of 5 requests:", [tb.allow() for _ in range(5)])
    time.sleep(1.1)
    print("After 1.1s wait    :", tb.allow())
