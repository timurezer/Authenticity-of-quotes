import sys

def matr(x, n, m):
    for i in range(n):
        for j in range(m):
            print(x[i][j], end=' ')
        print()
    print()

def turtle_adventures(c, n, m):
    d = [[float('inf') for i in range(m)] for j in range(n)]
    d[0][0] = c[0][0]
    for i in range(1, n):
        d[i][0] = d[i-1][0] + c[i][0]
    #matr(d, n, m)
    for j in range(1, m):
        d[0][j] = d[0][j-1] + c[0][j]
    #matr(d, n, m)
    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = min(d[i][j], d[i-1][j] + c[i][j], d[i][j-1] + c[i][j])
    #matr(d, n, m)
    return d[n-1][m-1]

def main():
    n, m = map(int, input().split())
    c = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    #matr(c, n, m)
    res = turtle_adventures(c, n, m)
    print(res)

if __name__ == '__main__':
    main()
'''
1 4
1 2 3 4
'''
