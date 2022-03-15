import sys, threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

'''
     ,--<---<----<--.
0 -> 1 -> 2 -> 3 -> 4

стартуем с 0, дойдем до 4, увидим 1, создали [1, 4], передали наверх,
добавили 3, и тд до 1, передали в tuple и возвращаем дальше.
Типо рекурсивные вызовы:
v
0    got (1,4,3,2),      return (1,4,3,2)
1    got [1,4,3,2],      return (1,4,3,2)
2    got [1,4,3],        return [1,4,3,2]
3    got [1,4],          return [1,4,3]
4 -> find 1,             return [1,4]

'''

def dfs(v, cur_color):
    #print(v, 'color =', cur_color)
    used[v] = 1
    colors[v] = cur_color
    ans = True
    for u in edges[v]:
        if used[u] == 1:  # если нашли цикл
            #print('found', v, u)
            return [v, u]   # такое ребро лежит в цикле, кладем u на 2е место в списке
        elif used[u] == 0:
            ans = dfs(u, cur_color * (-1))
            if isinstance(ans, list):
                # если это лист, есть цикл и мы не добрались до вершины u, в которую. воткнулись их v
                # тут хитрая проверка, когда нашли цикл, положили 1м в список номер вершины, в которой уже были,
                # поднимаемся по рекурсии наверх и смотрим, что получили
                if ans[1] != v:
                    ans.append(v)   # кладем в конец, когда соберем ответ - перевернем
                    #print(ans)
                else:
                    # тогда добрались в вершину, в которую мы воткнулись из v и нашли цикл
                    # передалаем ответ в tuple, тем самым isinstance дальше не будет давать true
                    # и не будут добавляться нвоые элементы в список вершин в цикле
                    ans = tuple(ans)
                    #print(ans)
                break
            if isinstance(ans, tuple):  # если tuple, то цикл нашли, он в ans, надо выйти из цикла по edges[v]
                break
    used[v] = 2
    return ans

def ans_return(n):
    for v in range(1, n+1):     # надо с 1
        if used[v] == 0:
            ans = dfs(v, 1)
            if isinstance(ans, tuple):
                return ans
    return 'NO'

def main():
    n, m = map(int, input().split())
    global edges, used, colors
    edges = [[] for i in range(n+1)]
    used = [0] * (n+1)      # 0 - white, 1 - grey, 2 - black vertex
    colors = [None] * (n+1)    # colors will be +1 and -1
    for i in range(m):
        x, y = map(int, input().split())
        edges[x].append(y)
    ans = ans_return(n)
    if isinstance(ans, str):
        print(ans)
    else:
        print('YES')
        sys.stdout.write(' '.join(map(str, ans)))


main_thread = threading.Thread(target= main )
main_thread.start()
main_thread.join()

'''
9 9
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
