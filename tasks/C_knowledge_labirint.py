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
    used = [False] * (n + 1)
    print(parents)
    cur = n
    used[cur] = True
    while cur > 0:  # 0 or 1 ?
        print(cur)
        print(used)
        cur = parents[cur]
        if not used[cur]:
            used[cur] = True
        else:
            print('here', cur)
            print(used)
            return ':)'
        if cur == -1:   # не добраться, иначе 0 и мы добрались до 1
            return ':('

    return d[-1]
    # а теперь проверим, есть ли цикл положительной длинны
    # for v in range(1, n + 1):
    #     for u, w in edges[v]:
    #         if d[u] < d[v] + w:     # если нашли что изменить -> есть цикл!
    #             return   # так обозначим цикл
    # return d[-1]

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
5 4
1 2 1
2 3 1
3 4 1
4 2 1

'''
