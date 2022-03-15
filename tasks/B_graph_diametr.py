import sys

def Floyd():
    d = w
    # начальные данные
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if d[i][j] == -1:
                d[i][j] = float('inf')
    # сам Флойд
    for k in range(1, n + 1):
        for v in range(1, n + 1):
            for u in range(1, n + 1):
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])
    return d

def diam_rad(d):
    eccentr_v = [0] * (n+1)     # для каждой вершины считаем эксцентриситет
    for i in range(1, n + 1):
        eccentr_v[i] = max(d[i][1:])    # тут слайсы, потому что нумерация вершин начинается с 1
    diam = max(eccentr_v[1:])   # максимум средим максимумов - диаметр
    rad = min(eccentr_v[1:])    # минимум среди максимумов - радиус
    return diam, rad

def main():
    global n, w
    n = int(input())
    w = [[None]*(n+1) for j in range(n+1)]
    for i in range(1, n+1):
        w[i] = [None] + list(map(int, sys.stdin.readline().split()))
    d = Floyd()
    diam, rad = diam_rad(d)
    print(diam)
    print(rad)
    print(w)
if __name__ == '__main__':
    main()
'''
4
0 3 1 -1
3 0 -1 4
1 -1 0 2
-1 4 2 0
-1 -1 -1 -1
'''
