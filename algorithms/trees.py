"""Trees, Heaps aur Tries - interview ke favourite topics."""


# ---------- Binary Search Tree ----------
class BST:
    class Node:
        def __init__(self, key):
            self.key, self.left, self.right = key, None, None

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BST.Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def inorder(self):
        out = []
        def walk(n):
            if n:
                walk(n.left); out.append(n.key); walk(n.right)
        walk(self.root)
        return out

    def height(self):
        def h(n):
            return 0 if n is None else 1 + max(h(n.left), h(n.right))
        return h(self.root)

    def search(self, key):
        n = self.root
        while n:
            if key == n.key:
                return True
            n = n.left if key < n.key else n.right
        return False


# ---------- Min Heap ----------
class MinHeap:
    def __init__(self):
        self.a = []

    def push(self, x):
        a = self.a
        a.append(x)
        i = len(a) - 1
        while i and a[(i - 1) // 2] > a[i]:
            a[(i - 1) // 2], a[i] = a[i], a[(i - 1) // 2]
            i = (i - 1) // 2

    def pop(self):
        a = self.a
        a[0], a[-1] = a[-1], a[0]
        top = a.pop()
        i = 0
        while True:
            l, r, s = 2 * i + 1, 2 * i + 2, i
            if l < len(a) and a[l] < a[s]: s = l
            if r < len(a) and a[r] < a[s]: s = r
            if s == i:
                break
            a[i], a[s] = a[s], a[i]
            i = s
        return top

    def __len__(self):
        return len(self.a)


def heap_sort(items):
    h = MinHeap()
    for x in items:
        h.push(x)
    return [h.pop() for _ in range(len(h))]


# ---------- Trie ----------
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word):
        node = self._find(word)
        return bool(node and "$" in node)

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def words_with_prefix(self, prefix):
        node, out = self._find(prefix), []
        def walk(n, path):
            for k, v in n.items():
                if k == "$":
                    out.append(prefix + path)
                else:
                    walk(v, path + k)
        if node:
            walk(node, "")
        return sorted(out)

    def _find(self, s):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node


def demo():
    t = BST()
    for x in [50, 30, 70, 20, 40, 60, 80]:
        t.insert(x)
    print("BST inorder :", t.inorder())
    print("BST height  :", t.height(), "| search 60:", t.search(60), "| search 65:", t.search(65))
    print("Heap sort   :", heap_sort([9, 4, 7, 1, 8, 2]))
    tr = Trie()
    for w in ["car", "card", "care", "cat", "dog"]:
        tr.insert(w)
    print("Trie 'ca*'  :", tr.words_with_prefix("ca"))
    print("Trie search 'car':", tr.search("car"), "| 'ca':", tr.search("ca"))
