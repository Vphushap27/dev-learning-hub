"""Graph algorithms: BFS, DFS, Dijkstra."""
import heapq
from collections import deque


def bfs(graph, start):
    seen, order, q = {start}, [], deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return order


def dfs(graph, start, seen=None):
    seen = set() if seen is None else seen
    seen.add(start)
    order = [start]
    for nxt in graph.get(start, []):
        if nxt not in seen:
            order += dfs(graph, nxt, seen)
    return order


def dijkstra(graph, start):
    """graph: {node: [(neighbor, weight), ...]} -> shortest distances."""
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float("inf")):
            continue
        for nxt, w in graph.get(node, []):
            nd = d + w
            if nd < dist.get(nxt, float("inf")):
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist


def demo():
    g = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": ["F"], "E": ["F"], "F": []}
    print("BFS:", bfs(g, "A"))
    print("DFS:", dfs(g, "A"))
    wg = {"A": [("B", 4), ("C", 1)], "C": [("B", 2), ("D", 7)], "B": [("D", 1)], "D": []}
    print("Dijkstra from A:", dijkstra(wg, "A"))
