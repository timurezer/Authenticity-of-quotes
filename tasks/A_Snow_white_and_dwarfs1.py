import sys

def dwarf_check(n, a, b):
    sn = 0
    for i in range(n):
        sn += a[i]
    c = [(a[i], b[i], i+1) for i in range(n)]
    c.sort(key=lambda x: x[0]+x[1], reverse= True)
    res = [0]*n
    for i in range(n):
        sn -= c[i][0]
        if sn >= c[i][1]:
            return -1
        else:
            res[i] = c[i][2]
    return res

def main():
    n = int(sys.stdin.readline())
    # structure: (index j, prefix sum S_j(a), b_j, a_j+b_j)
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    check = dwarf_check(n, a, b)
    if check != -1:
            print(*check)
    else:
        print(-1)


if __name__ == '__main__':
    main()
