import sys

def dwarf_check(n, a):
    a.sort(key= lambda x: x[-1], reverse= True)     # sort by a_j+b_j
    for i in range(1, n):   # create prefix sum of a's
        a[i][1] += a[i-1][1]
    res = [0]*n
    sn = a[n-1][1]
    for i in range(n):
        if sn-a[i][1] >= a[i][2]:
            return -1
        else:
            res[i] = a[i][0]
    return res

def main():
    n = int(sys.stdin.readline())
    # structure: (index j, prefix sum S_j(a), b_j, a_j+b_j)
    a = list(map(lambda x: [0, int(x), 0, 0], sys.stdin.readline().split()))
    i = 0
    for x in sys.stdin.readline().split():
        a[i][0] = i + 1
        a[i][2] = int(x)
        a[i][3] = a[i][1] + a[i][2]
        i += 1
    res = ''
    check = dwarf_check(n, a)
    if check != -1:
        print(*check)
        #for x in check:
        #    res += str(x) + ' '
    else:
        print(-1)


if __name__ == '__main__':
    main()
