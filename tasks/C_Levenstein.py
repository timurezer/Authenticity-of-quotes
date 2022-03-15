import sys

def l_distance(a, b):
    n = len(a)
    m = len(b)
    d = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = i
    for j in range(1, m + 1):
        d[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m + 1):
            d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
            if a[i-1] == b[j-1]:
                d[i][j] = min(d[i][j], d[i-1][j-1])
    matr(d, n+1, m+1)
    return d[n][m]

def matr(x, n, m):
    for i in range(n):
        for j in range(m):
            print(x[i][j], end=' ')
        print()
    print()


def main():
    a = sys.stdin.readline()
    b = sys.stdin.readline()
    print(l_distance(a, b))

main()
