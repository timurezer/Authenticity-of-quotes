from collections import deque
import sys


def bfs(v1):
    used = [False] * (n+1)
    d = [float('inf')] * (n+1)
    d[v1] = 0
    q = deque([v1])
    while len(q) != 0:
        v = q.popleft()
        # print('v =', v)
        # print('d[v] =', d[v])
        # print(used)
        used[v] = True
        for u in edges[v]:
            if not used[u]:
                # print('u', u)
                q.append(u)
                used[u] = True
                d[u] = d[v] + 1
                # print('d[v] =', d[v],'d[u] =', d[u])
    # print(d)
    return d


def compare(v, nearest, min_dist, new_dist):
    for i in range(1, n+1):
        if new_dist[i] < min_dist[i]:
            min_dist[i] = new_dist[i]
            nearest[i] = v
        elif new_dist[i] == min_dist[i] and v < nearest[i]:
            nearest[i] = v


def main():
    global edges, exits, n, m, k
    n = int(input())
    k = int(input())
    exits = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    edges = [[] for i in range(1 + n)]
    for i in range(m):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)
    min_dist = [float('inf')] * (n+1)
    nearest = [-1] * (n+1)
    for v in exits:
        new_dist = bfs(v)
        compare(v, nearest, min_dist, new_dist)

    sys.stdout.write(' '.join(map(str, min_dist[1:]))+'\n')
    sys.stdout.write(' '.join(map(str, nearest[1:])))

main()
