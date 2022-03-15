from collections import deque
import sys

def edges_create():
    edges = {}
    lett = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(1, 9):
        for j in range(1, 9):
            edges[lett[i]+str(j)] = []
    for i in range(1, 9):
        for j in range(1, 9):
            for k in range(-2, 3):
                for l in range(-2, 3):
                    if abs(k) + abs(l) == 3 and 1 <= i+k <= 8 and 1 <= j+l <= 8:
                        edges[lett[i]+str(j)].append(lett[i+k]+str(j+l))
    return edges

def bfs():
    global d
    edges = edges_create()
    used = {x: False for x in edges.keys()}
    q = deque([])
    q.append(v1)
    used[v1] = True
    while len(q) != 0:
        v = q.popleft()
        for u in edges[v]:
            if not used[u]:
                parent[u] = v
                q.append(u)
                used[u] = True
        if u == v2:
            return


def recover():
    res = []
    cur = v2
    while cur != -1:
        res.append(cur)
        cur = parent[cur]
    return res

def main():
    global v1, v2, n, parent
    n = 64
    v1 = str(input())
    v2 = str(input())
    parent = {}
    parent[v1] = -1
    bfs()
    res = recover()[::-1]
    sys.stdout.write('\n'.join(map(str, res)))

main()
