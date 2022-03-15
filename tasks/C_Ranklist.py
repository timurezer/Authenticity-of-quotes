from operator import itemgetter

def multisort(s, spec):
    for key, reverse in spec[::-1]:
        s.sort(key = itemgetter(key), reverse = reverse)
    return s

'''
def search_start(s: list, n: int,x: tuple):     # right side is not involved
    i, j = 0, n
    while j - i > 0:
        m = (i+j)//2
        if s[m][0] < x[0]:  # go to left
            j = m
        elif s[m][0] > x[0]:    # go to right
            i = m
        else:
            if s[m][1] >= x[1]:     # fo to left
                j = m
            else:
                i = m
    return j
'''
def main():
    n, k = map(int, input().split())
    s = []
    for i in range(n):
        a, b =  map(int, input().split())
        s.append(tuple([a, b]))
    s = multisort(s, ((0, True), (1, False)))
    #print(s, '\n', s[k-1])
    x = s[k-1]
    #print(search_start(s, n, s[k-1]))
    left = k-1
    while s[left] == x:
        if left - 1 >= 0: left -= 1
        else:
            left -= 1
            break
    left += 1

    right = k - 1
    while s[right] == x:
        if right+1 < n: right += 1
        else:
            right += 1
            break
    print(-left + right)



if __name__ == '__main__':
    main()

'''
6 1
3 1
3 2
5 3
3 1
3 7
2 1
'''
