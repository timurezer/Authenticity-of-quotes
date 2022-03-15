import sys
import heapq

def prime():
    d = [float('inf')] * (n + 1)
    used = [False] * (n + 1)
    d[1] = 0
    q = [(d[1], 1)]
    while len(q) != 0:
        d_cur, v = heapq.heappop(q)
        if d[v] < d_cur:
            continue
        used[v] = True
        for u, w in edges[v]:
            if d[u] > w and not used[u]:
                d[u] = w
                heapq.heappush(q, (w, u))
    return sum(d[1:])


def main():
    global n, edges
    n, m = map(int, input().split())
    edges = [[] for i in range(n + 1)]
    for _ in range(m):
        b, e, w = map(int, input().split())
        edges[b].append((e, w))
        edges[e].append((b, w))
    print(prime())

main()
