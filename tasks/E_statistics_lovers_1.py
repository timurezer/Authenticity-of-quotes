import sys

def left_bin_search(s_sorted, n, x):    # дает индекс левая границф, где числа >= x
    left, right = -1, n - 1
    while right - left > 1:
        m = (left + right)//2
        if s_sorted[m] < x:
            left = m
        elif s_sorted[m] >= x:
            right = m
    return right

def right_bin_search(s_sorted, n, x):    # дает индекс правой границы, где числа =< x
    left, right = 0, n
    while right - left > 1:
        m = (left + right)//2
        if s_sorted[m] <= x:
            left = m
        elif s_sorted[m] > x:
            right = m
    return left

def search(sx, left, right):    # find if there are items inside left-right bound
    #print(sx)
    n = len(sx)
    i = left_bin_search(sx, n, left)
    j = right_bin_search(sx, n, right)
    #print('i=', i, 'j=', j)
    res = True
    if i == n - 1:  # может дать индекс на самое правое число, которое меньше чем left
        if sx[i] < left:
            #print('left!!')
            res = False
    if j == 0:  # может дать индекс на самое левое число, которое больше чем right
        if sx[j] > right:
            #print('right!')
            res = False
    if i > j:   # если в наш интервал left-right не попало номеров городов, то i будет индекс на город справа, а j - слева
        res = False
    return res


def main():
    n = int(sys.stdin.readline())
    s = dict()
    i = 1
    for x in sys.stdin.readline().split():
        if int(x) in s: s[int(x)].append(i)
        else: s[int(x)] = [i]
        i += 1
    #print(s)
    q = int(sys.stdin.readline())
    res = ''
    for j in range(q):
        left, right, x = map(int, sys.stdin.readline().split())
        if x in s:
            #print(search(s[x], left, right))
            if search(s[x], left, right):
                res += '1'
            else:
                res += '0'
        else:
            res += '0'
    sys.stdout.write(res)


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
