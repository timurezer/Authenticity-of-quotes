import sys
import itertools

def nextRand24(a, b, m):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield (cur >> 8) % m

def left_bin_search(s_sorted, n, x):    # левая граница, где начинаются (i,x)
    left, right = -1, n - 1
    while right - left > 1:
        m = (left + right)//2
        #print('left=', left, 'right=', right, 'm=', m, 's[m]=', s_sorted[m])
        if s_sorted[m] < x:     # add [1]
            left = m
        elif s_sorted[m] >= x:   # add [1]
            right = m
    # return right      # Чтобы нашелся самый левый индекс на число >= х, надо просто вернуть right
    if s_sorted[right] == x:    # проверка, чтобы нашелся именно равный.
        return right
    else:
        return -1

def inv_count(s1, n):
    s2 = sorted(s1)
    invers_numb = 0
    for x in s1:
        #print(x)
        i = left_bin_search(s2, n, x)
        invers_numb += i
        del s2[i]
        n -= 1
    return invers_numb

def main():
    n, m = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())
    s = list(itertools.islice(nextRand24(a, b, m), n)) # x - данный массив
    #print(s)
    sys.stdout.write(str(inv_count(s, n))+'\n')



if __name__ == '__main__':
    main()
'''
20 5
19 18

'''
