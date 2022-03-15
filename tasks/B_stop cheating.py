import sys, threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def dfs(v, cur_color):
    # print(v,'color =' ,cur_color)
    used[v] = 1
    colors[v] = cur_color
    ans = True  # можно ли покрасить в 2 цвета
    for u in edges[v]:
        if used[u] == 0:
            ans &= dfs(u, cur_color * (-1))
            if not ans:     # если в одной из веток нельзя
                break   # выходим из цикла и возвращаем ответ
        elif used[u] == 1:  # обрабатываемая вершина
            if cur_color == colors[u]:  # если покрасить нельзя
                return False
    used[v] = 2
    return ans

def cheating(n):
    for v in range(1, n+1):
        if used[v] == 0:
            ans = dfs(v, 1)
            if ans == False:
                return 'No'
    return 'Yes'

def main():
    n, m = map(int, input().split())
    global edges, used, colors
    edges = [[] for i in range(n+1)]
    used = [0] * (n+1)      # 0 - white, 1 - grey, 2 - black vertex
    colors = [None] * (n+1)    # colors will be +1 and -1
    for i in range(m):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)
    print(cheating(n))



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
