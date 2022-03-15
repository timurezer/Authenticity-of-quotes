import sys
from random import randint
import itertools


def nextRand24(a, b):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield cur >> 8


def nextRand32(a, b):
    gen = nextRand24(a, b)
    while True:
        c = next(gen)
        d = next(gen)
        yield (c << 8) ^ d


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def Partition(a, l, r):
    l_cur, i = l, l
    r_cur = r
    x = a[randint(l, r)]
    while i <= r_cur:
        if a[i] < x:
            swap(a, i, l_cur)
            l_cur += 1
            i += 1
        elif a[i] == x:
            i += 1
        elif a[i] > x:
            swap(a, i, r_cur)
            r_cur -= 1
    return l_cur, r_cur


def order_stat_rec(a, l, r, q):
    l_cur, r_cur = Partition(a, l, r)
    res = 0
    if q < l_cur:
        res = order_stat_rec(a, l, l_cur - 1, q)
    elif q > r_cur:
        res = order_stat_rec(a, r_cur + 1, r, q)
    else:
        res = a[q]
    return res


def order_stat_iter(a, l, r, q):
    l_cur, r_cur = Partition(a, l, r)
    while not l_cur <= q <= r_cur:
        if q < l_cur:
            l_cur, r_cur = Partition(a, l, l_cur - 1)
        elif q > r_cur:
            l_cur, r_cur = Partition(a, r_cur + 1, r)
    return a[q]


def main():
    n, q = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())
    s = list(itertools.islice(nextRand32(a, b), n))
    sys.stdout.write(str(order_stat_rec(s, 0, n - 1, q - 1))+'\n')
    #sys.stdout.write(str(order_stat_iter(s, 0, n - 1, q - 1))+'\n')

if __name__ == '__main__':
    main()
