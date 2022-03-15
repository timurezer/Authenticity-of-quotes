import sys
#sys.setrecursionlimit(15000)

from _continuation import continulet

def invoke (_, callable , arg) :
    return callable (* arg)

def bootstrap(c) :
    callable, *arg = c.switch()
    while True :
        to = continulet(invoke, callable , arg )
        callable, *arg = c.switch (to=to)
cont = continulet(bootstrap)
cont.switch()

def dfs(v, edges, used, dp):
    used[v] = True
    if edges[v]:
        for u in edges[v]:
            if not used[u]:
                cont.switch(dfs(u, edges, used, dp))
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
