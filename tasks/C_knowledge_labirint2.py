import sys

def ford_bellman():
    d = [-float('inf')] * (n + 1)
    parents = [-1] * (n + 1)
    d[1] = 0
    parents[1] = 0
    for k in range(1, n):
        for v in range(1, n + 1):
            for u, w in edges[v]:
                if d[u] < d[v] + w:
                    d[u] = d[v] + w
                    parents[u] = v
    # print(parents)
    v_cycle = -1
    # а теперь проверим, есть ли цикл положительной длинны
    for v in range(1, n + 1):
        for u, w in edges[v]:
            if d[u] < d[v] + w:     # если нашли что изменить -> есть цикл!
                v_cycle = u
    if v_cycle != -1:
        return d[-1]
    else:
        cycle = set([])
        while v_cycle not in cycle:
            cycle.add(v_cycle)
            v_cycle = parents[v_cycle]
        print(cycle)

def main():
    global n, m, edges
    n, m = map(int, input().split())
    edges = [[] for i in range(n + 1)]
    for i in range(m):
        *rooms, w = map(int, sys.stdin.readline().split())
        edges[rooms[0]].append((rooms[1], w))
    res = ford_bellman()
    if res == None:   # есть положительный цикл
        print(':)')
    elif res == -float('inf'):     # нельзя добраться
        print(':(')
    else:
        print(res)


if __name__ == '__main__':
    main()

'''
4 4
1 2 1
2 3 2
3 1 3
3 4 1

'''
'''
6 6
1 2 1
2 3 2
3 1 3
3 4 1
1 5 1
5 6 1
'''
'''
6 6
1 2 1
2 3 1
3 4 1
4 2 1
1 5 1
5 6 1

'''
'''
5 5
1 2 1
2 3 1
3 4 1
4 2 1
2 5 1
'''
'''
5 5
1 2 1
2 3 1
3 4 1
4 2 1
5 2 1

'''
