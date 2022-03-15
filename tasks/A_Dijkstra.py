import sys
import heapq

def dijkstra(s, f):
    d = [float('inf')] * (n+1)
    q = [(0, s)]
    d[s] = 0
    while len(q) != 0:
        d_cur, v = heapq.heappop(q)
        # print((d_cur, v))
        if v == f:
            return d[v]
        if d_cur > d[v]:
            continue
        for u in range(1, n + 1):
            if w[v][u] != -1 and d[u] > d[v] + w[v][u]:
                d[u] = d[v] + w[v][u]
                heapq.heappush(q, (d[u], u))
    return -1

def main():
    global n, w
    n, s, f = map(int, input().split())
    w = [[] for j in range(n+1)]
    for i in range(1, n+1):
        w[i] = [None] + list(map(int, sys.stdin.readline().split()))
    res = dijkstra(s, f)
    sys.stdout.write(str(res))

if __name__ == '__main__':
    main()

'''
3 1 2
0 -1 2
3 0 -1
-1 4 0
'''

'''
3 1 2
0 -1 -1
3 0 -1
-1 4 0
'''
'''
5 1 5
0 1 1 1 -1
1 0 -1 -1 7
1 -1 0 -1 6
1 -1 -1 0 -1
-1 7 6 -1 0
'''
