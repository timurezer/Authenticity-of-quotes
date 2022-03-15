import sys
import itertools
from collections import deque

def nextRand24(a, b, m):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield (cur >> 8) % m

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

def merge_and_count(a, n, b, m):
    res = []
    inv_numb = 0
    b_cur_numb = 0      # сколько элементов b уже положили
    i, j = 0, 0
    while i < n and j < m:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
            inv_numb += b_cur_numb    # инверсию образуют очередной a_i и все b_j, которые уже лежат
        else:
            res.append(b[j])    # когда кладем b, то он не образует инверсии с элементами a_iб которые уже лежат
            j += 1
            b_cur_numb += 1
    res += a[i:]; inv_numb += (n - i)*b_cur_numb    # добавить все оставшиеся инверсии
    res += b[j:]
    return res, inv_numb

def mergesort_iter_inv_count(s: list, n: int):
    lenq = count_degree2(n)
    numb_of_zeros = lenq - n
    q = deque(
        [[0] for i in range(numb_of_zeros)] + [[x] for x in s]
    )
    inv_numb = 0
    while lenq > 1:
        a = q.popleft()
        b = q.popleft()
        cur_len = len(a)
        merged, addit_inv = merge_and_count(a, cur_len, b, cur_len)
        #print(addit_inv)
        q.append(merged)
        inv_numb += addit_inv
        lenq -= 1
    return inv_numb


def main():
    n, m = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())
    s = list(itertools.islice(nextRand24(a, b, m), n)) # x - данный массив
    print(s)
    total_inv = mergesort_iter_inv_count(s, n)
    sys.stdout.write(str(total_inv)+'\n')


if __name__ == '__main__':
    main()
