from collections import deque
from random import randint


def merge(a, n, b, m):
    res = []
    i, j = 0, 0
    while i < n and j < m:
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res += a[i:]
    res += b[j:]
    return res

def mergesort_rec(s: list, n: int):
    if n <= 1:
        return s
    n_new = n//2
    a = mergesort_rec(s[0: n_new], n_new)
    b = mergesort_rec(s[n_new:], n - n_new)
    return merge(a, n_new, b, n - n_new)


def count_degree2(x):
    res = 0
    x1 = x
    while x1 != 1:
        x1 //= 2
        res += 1
    y = 2**res
    if y < x:
        y *= 2
    return y


def mergesort_iter(s: list, n: int):
    lenq = count_degree2(n)
    numb_of_zeros = lenq - n
    q = deque(
        [[0] for i in range(numb_of_zeros)] + [[x] for x in s]
    )

    while lenq > 1:
        a = q.popleft()
        b = q.popleft()
        cur_len = len(a)
        q.append(merge(a, cur_len, b, cur_len))
        lenq -= 1
    return q.pop()[numb_of_zeros:]


def main():
    n = 16
    s1 = [randint(0, 10) for i in range(n)]
    s2 = [x for x in s1]
    #print(s1)

    s1 = mergesort_iter(s1, n)
    s2.sort()
    #print('my_sort:', s1)
    #print('not_myy:', s2)
    if s1 == s2:
        print('Yes')
    else:
        print('No')

def main2():
    print(count_degree2(1023))

if __name__ == '__main__':
    main()
