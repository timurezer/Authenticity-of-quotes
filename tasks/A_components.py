import sys, threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def dfs(v):
    used[v] = True
    comp_vertex[v] = comp_number
    for u in edges[v]:
        if not used[u]:
            dfs(u)


def main():
    n, m = map(int, input().split())
    global edges, used, comp_number, comp_vertex
    edges = [[] for i in range(n+1)]
    used = [False] * (n+1)
    comp_vertex = [0] * (n+1)
    for i in range(m):
        x, y = map(int, input().split())
        edges[x].append(y)
        edges[y].append(x)
    comp_number = 0
    for v in range(1, n+1):
        if not used[v]:
            comp_number += 1
            #print(comp_number)
            dfs(v)
    print(comp_number)
    sys.stdout.write(' '.join(map(str, comp_vertex[1:])))

main_thread = threading.Thread(target= main )
main_thread.start()
main_thread.join()
