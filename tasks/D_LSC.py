import sys

def lcs(n, a, m ,b):
    d = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1])
    #matr(d, n + 1, m + 1)
    res = maxi(d, n + 1, m + 1)
    return(res)

def maxi(d, n, m):
    maxel = -1
    for i in range(n):
        for j in range(m):
            if d[i][j] > maxel:
                maxel = d[i][j]
    return maxel

def matr(x, n, m):
    for i in range(n):
        for j in range(m):
            print(x[i][j], end=' ')
        print()
    print()

def main():
    n = int(input())
    a = list(sys.stdin.readline().split())
    m = int(input())
    b = list(sys.stdin.readline().split())
    res = lcs(n, a, m, b)
    print(res)

main()
