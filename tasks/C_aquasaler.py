import sys

def find_min(arr, n):   # находит минимум и его позицию в массиве
    cur_min = float('inf')
    cur_pos = 0
    for i in range(n):
        if cur_min > arr[i]:
            cur_min = arr[i]
            cur_pos = i
    return cur_min, cur_pos

def get(v, s):
    x = (s >> v) & 1
    return x == 1

def commis_voyager(start, n, l, dp):
    for s in range(1 << n):
        if not get(start, s):
            continue
        for v in range(n):
            if not get(v, s):
                continue
            for u in range(n):
                if u != v and get(u, s):
                    y = dp[s - (1 << v)][u] + l[u][v]
                    dp[s][v] = min(dp[s][v], y)
    return find_min(dp[(1 << n) - 1], n)
    # выдаем вершину, в которой остановились (она будет началом или концом пути, у нас симметрия), и длину пути

def recover(dp, l, n, min_ind):     # просто идем в обратном порядке по dp и понимаем, откуда пришли
    s = (1 << n) - 1
    v = min_ind     # стартуем из последней вершины, найденной в предыдущей функции
    res = [v + 1]
    for i in range(n):
        for u in range(n):
            if u != v and get(u, s):
                if dp[s][v] == dp[s - (1 << v)][u] + l[u][v]:
                    s -= (1 << v)
                    v = u
                    res.append(v + 1)
    return res

def main():
    n = int(sys.stdin.readline())
    l = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    # чтобы найти оптимальный путь, надо перебрать все возможные начала пути, будем сразу восстанавливать ответ
    anses = []
    for start in range(n):
        dp = [[float('inf') for i in range(n)] for j in range(1 << n)]
        dp[1 << start][start] = 0   # стартуем с такой маски и такой вершины
        summ, min_ind = commis_voyager(start, n, l, dp)
        path = recover(dp, l, n, min_ind)   # восстанавливаем ответ
        anses.append((summ, path))
    right_answ = min(anses, key= lambda x: x[0])    # нам нужен тот ответ, у которого минимальная длина пути
    sys.stdout.write(str(right_answ[0])+'\n')
    sys.stdout.write(' '.join(map(str, right_answ[1])))

main()
