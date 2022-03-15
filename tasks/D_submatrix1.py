import sys

def add(h: list, sz: list, x: int):
    h.append(x)
    sz[0] += 1
    siftUp(h, sz)

def swap(h, i, j):
    h[i], h[j] = h[j], h[i]

def siftUp(h, sz: list):
    cur = sz[0] - 1    # index
    parent = (cur - 1) // 2
    while cur > 0 and h[cur] < h[parent]:
        swap(h, cur, parent)
        cur = parent
        parent = (cur - 1) // 2

def getMin(h):
    return h[0]

def exctactMin(h, sz):
    hmin = getMin(h)
    swap(h, 0, sz[0] - 1)
    del h[sz[0] - 1]
    sz[0] -= 1
    siftDown(h, sz)

def siftDown(h, sz):
    cur = 0
    child = 2*cur + 1
    while child < sz[0]:  # тут могло сломаться при обращении, если нет child выходит за границы, но все окей...
        if child + 1 < sz[0] and h[child + 1] < h[child]:    # и здесь
            child += 1
        if h[cur] <= h[child]:   # спомни как ты тут обосрался
            break
        swap(h, cur, child)
        cur = child
        child = 2*cur + 1

def delete(h_del, sz_del, x):
    add(h_del, sz_del, x)

def new_getMin(h, sz, h_del, sz_del):
    while sz[0]!=0 and sz_del[0]!=0 and getMin(h) == getMin(h_del):
        exctactMin(h, sz)
        exctactMin(h_del, sz_del)
    if sz!=0:
        return getMin(h)
    else:
        return -1

def new_extractMin(h, sz, h_del, sz_del):
    while sz[0]!=0 and sz_del[0]!=0 and getMin(h) == getMin(h_del):
        exctactMin(h, sz)
        exctactMin(h_del, sz_del)
    if sz!=0:
        return exctactMin(h, sz)
    else:
        return -1

def print_matrix(m, n, l):
    for i in range(n):
        for j in range(l):
            sys.stdout.write(str(m[i][j])+' ')
        sys.stdout.write('\n')

def make_heap1(h, sz, h_del, sz_del, m, i, j, l):
    if sz == [0]:
        for k in range(j, j + l):
                    add(h, sz, m[i][k])
    else:
        add(h_del, sz_del, m[i][j-1])
        add(h, sz, m[i][j + l - 1])

def make_heap2(h, sz, h_del, sz_del, m, i, j, l):
    if sz == [0]:
        for k in range(i, i + l):
                    add(h, sz, m[k][j])
    else:
        add(h_del, sz_del, m[i - 1][j])
        add(h, sz, m[i + l -1][j])


def main():
    n, l = map(int, sys.stdin.readline().split())
    m = [list(map(int, sys.stdin.readline().split())) for j in range(n)]
    res1 =[[0 for j in range(n - l + 1)] for i in range(n)]
    res2 = [[0 for j in range(n - l + 1)] for j in range(n - l + 1)]

    h, h_del = [], []
    sz, sz_del = [0], [0]

    for i in range(n):
        for j in range(0, n-l+1):
            #print(i, j)
            make_heap1(h, sz, h_del, sz_del, m, i, j, l)
            #print("h", h)
            #print('h_del', h_del)
            res1[i][j] = new_getMin(h, sz, h_del, sz_del)
        h, h_del = [], []
        sz, sz_del = [0], [0]

    for j in range(n - l + 1):
        for i in range( n-l+1):
            #print(i, j)
            make_heap2(h, sz, h_del, sz_del, res1, i, j, l)
            #print("h", h)
            #print('h_del', h_del)
            res2[i][j] = new_getMin(h, sz, h_del, sz_del)
        h, h_del = [], []
        sz, sz_del = [0], [0]

    print_matrix(res2, n - l + 1, n-l+1)

if __name__ == '__main__':
    main()

'''
4 2
4 5 3 2
1 2 5 4
3 4 2 3
1 3 5 5
'''
