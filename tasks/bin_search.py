def left_bin_search(s_sorted, n, x):    # левая граница, где начинаются (i,x)
    left, right = -1, n - 1
    while right - left > 1:
        m = (left + right)//2
        print('left=', left, 'right=', right, 'm=', m, 's[m]=', s_sorted[m])
        if s_sorted[m] < x:     # add [1]
            left = m
        elif s_sorted[m] >= x:   # add [1]
            right = m
    return right      # Чтобы нашелся самый левый индекс на число >= х, надо просто вернуть right
    # if s_sorted[right] == x:    # проверка, чтобы нашелся именно равный.
    #     return right
    # else:
    #     return -1


def right_bin_search(s_sorted, n, x):    # правая граница, где начинаются (i,x)
    left, right = 0, n
    while right - left > 1:
        m = (left + right)//2
        print('left=', left, 'right=', right, 'm=', m, 's[m]=', s_sorted[m])
        if s_sorted[m] <= x:     # add [1]
            left = m
        elif s_sorted[m] > x:   # add [1]
            right = m
    return left     # Чтобы нашелся самый индекс на число <= х, надо просто вернуть left
    # if s_sorted[left] == x:    # если нашелся
    #     return left
    # else:
    #     return -1

def main():
    s = [1, 2, 3, 30, 40]
    q = [-1, 0, 0, 0, 0, 1, 1, 1, 2]
    r = [-1]
    print(q)
    n = len(q)
    print(right_bin_search(q, len(q), 1))
    #print(right_bin_search(q, len(q), 2))

if __name__ =='__main__':
    main()



