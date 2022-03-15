import sys
import heapq

def prime():
    global p
    d = [float('inf')] * (n + 1)
    used = [False] * (n + 1)
    p = [-1] * (n + 1)
    d[1] = 0
    q = [(d[1], 1)]
    p[1] = 1
    while len(q) != 0:
        d_cur, v = heapq.heappop(q)
        if d[v] < d_cur:
            continue
        used[v] = True
        for u, w in edges[v]:
            if d[u] > w and not used[u]:
                d[u] = w
                heapq.heappush(q, (w, u))
                p[u] = v
    return sum(d[1:])

def dist(i, j):
    return ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)  ** 0.5

def main():
    global n, edges, points
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    edges = [[] for i in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
                x = dist(i, j)
                edges[i + 1].append((j + 1, x))
                edges[j + 1].append((i + 1, x))
    print(f'{prime():.6f}')
    print(n-1)
    for i in range(2, n+1):
        print(i, p[i])

main()
