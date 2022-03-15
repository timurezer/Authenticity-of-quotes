import sys

def cover(n, s, m):
    s.sort(key= lambda x: x[0])     # сортируем по левой границе
    print(s)
    l_prev, r_prev = 0, 0   # it will be section that will be added in answer
    l_cur, r_cur = 0, 0     # here will be candidates for the next prev.
    print(0)
    print('l_prev=', l_prev, 'r_prev=', r_prev)
    print('l_cur=', l_cur, 'r_cur=', r_cur)
    i = 0
    res = []
    l, r = s[i]
    #print(l, r)
    while i < n and l < m:
        l, r = s[i]
        print(l, r)
        while l <= r_prev and i < n:
            if r_cur < r:               # then update current. Current is our candidate
                l_cur, r_cur = l, r     # here r_cur may become > m, then we will see at the next while iteration
                print('new l_cur=', l_cur, 'r_cur=', r_cur)
            i += 1
            print(i)
            print('l_prev=', l_prev, 'r_prev=', r_prev)
            print('l_cur=', l_cur, 'r_cur=', r_cur)
        if i < n:
            if l <= r_prev:
                l_prev, r_prev = l_cur, r_cur   # update fixed section
                res.append((l_prev, r_prev))
                i += 1
            else:
                return 'No solution'    # получился разрыв
        else:
            if r_cur < m:
                return 'No solution'
            else:
                return res

    print(res)
    return res


def main():
    m = int(sys.stdin.readline())
    s = []
    l, r = map(int, sys.stdin.readline().split())
    n = 0
    while l != 0 or r != 0:
        s.append((l, r))
        l, r = map(int, sys.stdin.readline().split())
        n += 1
    res = cover(n, s, m)
    print(res)

if __name__ == '__main__':
    main()

'''
1
-1 0
-5 -3
2 5
0 0
'''
'''
1
-1 0
-5 -3
-1 0.5
2 5
0 0
'''
'''
-5 3
-4 -1
-4 0
-4 1
-3 0
-3 1
-5 -2
-1 2
0 2
0 4
0 0
'''
