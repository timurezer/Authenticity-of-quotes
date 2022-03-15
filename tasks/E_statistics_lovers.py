import sys

def main1(n, s, q):
    s = tuple(s)
    res = ''
    for i in range(q):
        left, right, x = map(int, sys.stdin.readline().split())
        res += check(s, left - 1, right - 1, x)
    sys.stdout.write(res)

def check(s, left, right, x):
    res = '0'
    for i in range(left, right + 1):
        if s[i] == x:
            res = '1'
            break
    return res

def main2(n, s, q):
    for j in range(n):    #input().split():
        x = s[j]
        s[j] = tuple([j+1, x])
        j+=1
    s_sorted = tuple(sorted(s, key = lambda x: x[1]))
    s = tuple(s)
    #print(s)
    #print(s_sorted)
    res = ''

    for i in range(q):
        left, right, x = map(int, sys.stdin.readline().split())
        i = left_bin_search(s_sorted, n, x)
        #print('i=', i, 'j=', j)
        ans = '0'
        if i != -1:
            j = right_bin_search(s_sorted, n, x)
            while i < j + 1:
                if left <= s_sorted[i][0] <= right:
                    ans = '1'
                    break
                else:
                    i += 1
        res += ans
    sys.stdout.write(res)

def left_bin_search(s_sorted, n, x):    # левая граница, где начинаются (i,x)
    left, right = -1, n - 1
    while right - left > 1:
        m = (left + right)//2
        #print('left=', left, 'right=', right, 'm=', m, 's[m]=', s_sorted[m])
        if s_sorted[m][1] < x:     # add [1]
            left = m
        elif s_sorted[m][1] >= x:   # add [1]
            right = m
    if s_sorted[right][1] == x:    # если нашелся  # add [x]
        return right
    else:
        return -1

def right_bin_search(s_sorted, n, x):    # левая граница, где начинаются (i,x)
    left, right = 0, n
    while right - left > 1:
        m = (left + right)//2
        #print('left=', left, 'right=', right, 'm=', m, 's[m]=', s_sorted[m])
        if s_sorted[m][1] <= x:     # add [1]
            left = m
        elif s_sorted[m][1] > x:   # add [1]
            right = m
    if s_sorted[left][1] == x:    # если нашелся
        return left
    else:
        return -1

def main():
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))   # cities
    q = int(sys.stdin.readline())
    if q < n//10:
        main1(n, s, q)
    else:
        main2(n, s, q)

if __name__ =='__main__':
    main()




'''
5
123 666 314 666 434
5
1 5 314
1 5 578
2 4 666
4 4 713
1 1 123
'''
'''
5
123 666 314 666 434
1
2 3 314
'''
'''
5
123 666 314 666 434
1
4 5 123
'''
'''
5
123 666 314 666 434
1
1 5 578

'''
