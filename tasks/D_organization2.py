from collections import deque
import sys

def bfs1(v1, edges, exits, n, m, k):
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

def compare1(v, nearest, min_dist, new_dist, n):
    for i in range(1, n+1):
        if new_dist[i] < min_dist[i]:
            min_dist[i] = new_dist[i]
            nearest[i] = v
        elif new_dist[i] == min_dist[i] and v < nearest[i]:
            nearest[i] = v

def main1(edges, exits, n, m, k):
    min_dist = [float('inf')] * (n+1)
    nearest = [-1] * (n+1)
    for v in exits:
        new_dist = bfs1(v, edges, exits, n, m, k)
        compare1(v, nearest, min_dist, new_dist, n)
    return (min_dist[1:], nearest[1:])

######################################################

def bfs(edges, exits, n, m, k):
    used = [False] * (n+1)
    d = [float('inf')]*(n+1)     # расстояние от ближайшей вершины эвакуации и сама ближайшая вершина эвакуации
    evacuations = [-1]*(n+1)
    for x in exits:
        d[x] = 0
        evacuations[x] = x
    q = deque([x for x in exits])  # (vertex , its evacuation lift number)
    # print(q)
    exits_set = set(exits)
    while len(q) != 0:
        v = q.popleft()
        # print('v =', v)
        # print('d[v] =', d[v])
        # print(used)
        used[v] = True
        for u in edges[v]:
            if not used[u] and u not in exits_set:
                # print('u', u)
                q.append(u)
                used[u] = True
                d[u] = d[v] + 1
                evacuations[u] = evacuations[v]
                # print(d[u])
                # print('d[v] =', d[v],'d[u] =', d[u])
    # print(d)
    return d, evacuations

def main2(edges, exits, n, m, k):
    min_dist, nearest = bfs(edges, exits, n, m, k)
    return (min_dist[1:], nearest[1:])

from random import randint

def main():
    for j in range(50):
        n = randint(2, 8)
        k = randint(1, n)
        exits = []
        for i in range(k):
            x = randint(1, n)
            if x not in exits:
                exits.append(x)
        exits.sort()
        m = randint(1, n*(n-1)//2)
        edges = [[] for i in range(1 + n)]
        for i in range(m):
            x, y = randint(1, n), randint(1, n)
            if y not in edges[x]:
                edges[x].append(y)
                edges[y].append(x)
        ans1 = main1(edges, exits, n, m, k)
        ans2 = main2(edges, exits, n, m, k)
        if not ans1 == ans2:
            print(n)
            print(k)
            print(exits)
            print(edges)
            print(ans1[0], ans2[0])
            print(ans1[1], ans2[1])
            break

main()
