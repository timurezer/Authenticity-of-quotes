import sys, threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def dfs(v, cur_color):
    #print(v, 'color =', cur_color)
    used[v] = 1
    colors[v] = cur_color
    ans = True
    for u in edges[v]:
        if used[u] == 1:  # если нашли цикл
            #print('found', v, u)
            return [u, v]   # такое ребро лежит в цикле, кладем u на 1е место в списке
        elif used[u] == 0:
            ans = dfs(u, cur_color * (-1))
            if isinstance(ans, list):
                if ans[0] != v:
                    ans.append(v)
                    #print(ans)
                else:
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
                return ans[::-1]
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
