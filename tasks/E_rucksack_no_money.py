import sys

def rocksuck(n, s, w):
    d = [[0 for i in range(s + 1)] for j in range(n + 1)]
    prev = [[0 for i in range(s + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            d[i][j] = d[i-1][j]
            if j - w[i-1] >= 0:
                d[i][j] = max(d[i][j], d[i-1][j - w[i-1]] + w[i-1])
                if d[i][j] == d[i][j]:
                    prev[i][j] = 0      # не положили, двигаемся в (i-1, j)
                else:
                    prev[i][j] = 1      # положили, двигаемся в (i-1, j - w[i-1])
    matr(d, n+1, s + 1)
    return d[n+1][s+1]

def matr(x, n, m):
    for i in range(n):
        for j in range(m):
            print(x[i][j], end=' ')
        print()

def main():
    s, n = map(int, input().split())
    w = list(map(int, sys.stdin.readline().split()))
    ans = rocksuck(n, s, w)
    print(ans)

main()
'''
7 4
2 3 4 1

9

'''
