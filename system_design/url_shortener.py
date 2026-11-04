"""URL Shortener core: Base62 encoding + in-memory store."""
import string

ALPHABET = string.digits + string.ascii_lowercase + string.ascii_uppercase


def encode(num):
    if num == 0:
        return ALPHABET[0]
    out = []
    while num:
        num, r = divmod(num, 62)
        out.append(ALPHABET[r])
    return "".join(reversed(out))


def decode(s):
    n = 0
    for ch in s:
        n = n * 62 + ALPHABET.index(ch)
    return n


class Shortener:
    def __init__(self, base="https://sho.rt/"):
        self.base, self.counter = base, 100000
        self.store = {}

    def shorten(self, url):
        self.counter += 1
        code = encode(self.counter)
        self.store[code] = url
        return self.base + code

    def resolve(self, short):
        return self.store.get(short.replace(self.base, ""))


def demo():
    s = Shortener()
    short = s.shorten("https://github.com/trending")
    print("Short   :", short)
    print("Resolved:", s.resolve(short))
