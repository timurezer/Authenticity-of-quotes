import sys, threading

# и это тоже с wiki
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def dfs(v, edges, used, dp):
    used[v] = True
    if edges[v]:
        for u in edges[v]:
            if not used[u]:
                dfs(u, edges, used, dp)
            dp[v] = max(dp[v], dp[u] + 1)

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = [[] for i in range(n + 1)]
    for i in range(m):
        v, u = map(int, sys.stdin.readline().split())
        edges[v].append(u)
    dp = [0] * (n + 1)
    used = [False] * (n + 1)
    for v in range(1, n + 1):
        if not used[v]:
            dfs(v, edges, used, dp)
    print(max(dp))

# эта фигня для того, чтобы глубина рекурсии была максимальной, это из технических советов с wiki
main_thread = threading.Thread(target= main )
main_thread.start()
main_thread.join()
