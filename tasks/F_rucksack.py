import sys

def rocksuck(n, s, w, c):
    d = [[0 for i in range(s + 1)] for j in range(n + 1)]
    prev = [[0 for i in range(s + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            d[i][j] = d[i-1][j]
            if j - w[i-1] >= 0:
                d[i][j] = max(d[i][j], d[i-1][j - w[i-1]] + c[i-1])
                if d[i][j] == d[i-1][j]:
                    prev[i][j] = 0      # не положили, двигаемся в (i-1, j)
                else:
                    prev[i][j] = 1      # положили, двигаемся в (i-1, j - w[i-1])
    #matr(d, n + 1, s + 1)
    #matr(prev, n+1, s + 1)

    cur = [n, s]
    res = []
    #print(cur)
    while cur[0] > 0:
        if prev[cur[0]][cur[1]] == 0:
            cur[0] -= 1
        else:
            res.append(cur[0])
            cur[1] -= w[cur[0]-1]
            cur[0] -= 1
        # print(cur)
    return res

def matr(x, n, m):
    for i in range(n):
        for j in range(m):
            print(x[i][j], end=' ')
        print()
    print()


def main():
    n, s = map(int, input().split())
    w = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    ans = rocksuck(n, s, w, c)
    print(len(ans))
    sys.stdout.write(' '.join(map(str, ans)))

main()
'''

'''
