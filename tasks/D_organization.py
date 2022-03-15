from collections import deque
import sys

def bfs():
    used = [False] * (n+1)
    d = [float('inf')]*(n+1)
    evacuations = [-1]*(n+1)    # массив с ближайшими выходами
    for x in exits:     # делаем во всех выходах 0 расстояние и ближайшего выхода - его же самого
        d[x] = 0
        evacuations[x] = x
    q = deque([x for x in exits])

    exits_set = set(exits)

    while len(q) != 0:
        v = q.popleft()
        used[v] = True
        for u in edges[v]:
            if not used[u] and u not in exits_set:  # дополнительная проверка, чтобы выходы выходов не портились
                q.append(u)
                used[u] = True
                d[u] = d[v] + 1
                evacuations[u] = evacuations[v]
    return d, evacuations

def main():
    global edges, exits, n, m, k
    n = int(input())
    k = int(input())
    exits = list(map(int, sys.stdin.readline().split()))
    exits.sort()    # надо отсортировать
    m = int(input())
    edges = [[] for i in range(1 + n)]
    for i in range(m):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)

    min_dist, nearest = bfs()
    sys.stdout.write(' '.join(map(str, min_dist[1:]))+'\n')
    sys.stdout.write(' '.join(map(str, nearest[1:])))

main()
'''
4
2
2 4
2
3 2
3 4
'''
'''
9 
2
5 0
9
0 1
1 2
2 3
1 4
4 5
5 6
6 4
1 7
7 8
0 9
'''


'''
7
3
2 3 1
6
1 4
4 7
2 5
5 7
3 6
6 7
'''


'''
4
2
4 3
2
1 2
1 3
'''

'''
2
1
1
1
1 2
'''
'''
3
1
2
1
1 2
'''
'''
2
1
2
1
1 2
'''
'''
5
1
4
5
1 2
1 3
1 4
3 5
3 4

'''
