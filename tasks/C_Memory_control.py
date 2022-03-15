import sys

def add(h: list, sz: list, x, d):
    h.append(x)
    sz[0] += 1
    i = siftUp(h, sz, d)
    return i

def swap(h, i, j, d):
    h[i], h[j] = h[j], h[i]
    d[h[i][0]], d[h[j][0]] = d[h[j][0]], d[h[i][0]]

def siftUp(h, sz, d):
    cur = sz[0] - 1    # index
    parent = (cur - 1) // 2
    # куча не в порядке, если или время открытия ребенка меньше чем у родителя, или при равных временах номер ребенка меньше чем у родителя
    while cur > 0 and (h[cur][1] < h[parent][1] or (h[cur][1] == h[parent][1] and h[cur][0] < h[parent][0])):
        swap(h, cur, parent, d)
        cur = parent
        parent = (cur - 1) // 2
    return cur

def getMin(h, sz):
    if sz[0] == 0:
        return -1
    else:
        return h[0]

def siftDown(h, sz, i, d):
    cur = i
    child = 2*cur + 1
    while child < sz[0]:  # тут могло сломаться при обращении, если нет child выходит за границы, но все окей...
        # надо обмениваться с ячейкой, у которой или меньшее время открытия, или меньший номер
        if child + 1 < sz[0] and \
                (h[child + 1][1] < h[child][1] or (h[child + 1][1] == h[child][1] and h[child + 1][0] < h[child][0])):    # и здесь
            child += 1
        if h[cur][1] < h[child][1] \
                or (h[cur][1] == h[child][1] and h[cur][0] < h[child][0]):   # спомни как ты тут обосрался
            break
        swap(h, cur, child, d)
        cur = child
        child = 2*cur + 1
    return cur

def main():
    dt = 600
    sz = [0]
    h = []
    d = dict()
    last_d = 0    # remember the number of the last blocked cell (the last item of d)
    request = sys.stdin.readline().split()
    while request:
        t_cur = int(request[0])
        print('h', h)
        if request[1] == '+':
            x = getMin(h, sz)
            print('getMin', x)
            print('d', d, 'last_d', last_d)
            if x == -1:     # all cells are free
                i = add(h, sz, [1, t_cur + dt], d)
                d[1] = i
                last_d = 1
                print('empty heap', 1)
                sys.stdout.write('1' + '\n')
            elif x[1] <= t_cur:     # this cell is free
                i = d[x[0]]    # curr position in heap
                h[i][1] = t_cur + dt    # update unlock time
                j = siftDown(h, sz, i, d)      # new position in heap, update d
                #d[x[0]] = j     # update info in dict
                print('update', h[j][0])
                sys.stdout.write(str(x[0])+'\n')
            elif x[1] > t_cur:
                x_last = last_d    # the last locked cell -> have to lock new
                n = x_last + 1       # number of new locked cell
                i = add(h, sz, [n, t_cur + dt], d)     # index of new cell in heap
                d[n] = i
                last_d = n
                print('next cell', n)
                sys.stdout.write(str(n)+'\n')
        else:
            print(request)
            n = int(request[2])
            if n not in d or h[d[n]][1] <= t_cur:
                sys.stdout.write('-' + '\n')
            else:
                sys.stdout.write('+' + '\n')
                h[d[n]][1] = t_cur + dt
                i = d[n]
                siftDown(h, sz, i, d)
        print('h', h)
        request = sys.stdin.readline().split()


if __name__ =='__main__':
    main()

'''
1 +
1 +
1 +
1 . 3
2 . 2
2 . 1
2 . 3

'''
'''

'''
