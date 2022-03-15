import sys
from collections import deque

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
        if h[cur] <= h[child]:
            break
        swap(h, cur, child)
        cur = child
        child = 2*cur + 1

def delete(h_del, sz_del, x):
    add(h_del, sz_del, x)

def new_getMin(h, sz, h_del, sz_del):
    while sz[0] != 0 and sz_del[0] != 0 and getMin(h) == getMin(h_del):
        exctactMin(h, sz)
        exctactMin(h_del, sz_del)
    if sz[0] != 0:
        sys.stdout.write(str(getMin(h))+'\n')
    else:
        sys.stdout.write(str(-1)+'\n')

def new_extractMin(h, sz, h_del, sz_del):
    while sz[0]!=0 and sz_del[0]!=0 and getMin(h) == getMin(h_del):
        exctactMin(h, sz)
        exctactMin(h_del, sz_del)
    return exctactMin(h, sz)


def main():
    q = int(sys.stdin.readline())
    Q = deque([])  # queue
    h = [] # main heap
    sz_h, sz_del = [0], [0]
    h_del = [] # del
    for i in range(q):
        a = sys.stdin.readline()
        if a[0] == '+':
            x = int(a[2:])
            Q.append(x)
            add(h, sz_h, x)
            new_getMin(h,sz_h, h_del, sz_del)
            #print(Q)
        else:
            x = Q.popleft()
            #print(Q)
            add(h_del, sz_del, x)
            new_getMin(h, sz_h, h_del, sz_del)
            #print(h_del)

if __name__ == '__main__':
    main()

