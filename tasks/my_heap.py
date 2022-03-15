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

# to delete elements from heap - cteate second heap for deleted elements
# if we mant to get min, we have to chech whether the min is deleted
# the min in second heap can't be less than in the main heap if all deleting comands were used for elements from hain heap
# otherwise we have to check wheter the element is in the main heap

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



def main():
    h = []  # my_heap
    sz_h = [0]    # fckn invariant const's
    h_del = []
    sz_del = [0]
    h = [1, 1, 1, 3, 4, 9, 10]
    sz_h = [len(h)]
    delete(h_del, sz_del, 1)
    delete(h_del, sz_del, 3)
    delete(h_del, sz_del, 1)
    delete(h_del, sz_del, 1)
    print(new_getMin(h, sz_h, h_del, sz_del))
    print(new_getMin(h, sz_h, h_del, sz_del))


if __name__ =='__main__':
    main()
