"""Consistent Hashing ring - distributed caches/DBs ke liye."""
import bisect
import hashlib


class HashRing:
    def __init__(self, nodes=(), replicas=50):
        self.replicas, self.ring, self.keys = replicas, {}, []
        for n in nodes:
            self.add(n)

    @staticmethod
    def _h(key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add(self, node):
        for i in range(self.replicas):
            h = self._h(f"{node}#{i}")
            self.ring[h] = node
            bisect.insort(self.keys, h)

    def get(self, key):
        h = self._h(key)
        idx = bisect.bisect(self.keys, h) % len(self.keys)
        return self.ring[self.keys[idx]]


def demo():
    ring = HashRing(["server-1", "server-2", "server-3"])
    for k in ["user:1", "user:2", "user:3", "user:4"]:
        print(f"{k} -> {ring.get(k)}")
