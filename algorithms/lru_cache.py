"""LRU Cache - O(1) get/put (classic interview + system design)."""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


def demo():
    c = LRUCache(2)
    c.put("a", 1); c.put("b", 2)
    print("get a ->", c.get("a"))
    c.put("c", 3)  # 'b' evict hoga
    print("get b ->", c.get("b"), "(evicted)")
    print("keys  ->", list(c.data))
