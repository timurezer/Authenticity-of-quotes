import sys
from collections import deque
import heapq

def new_getMin(h, sz, h_del, sz_del):
    while sz[0] != 0 and sz_del[0] != 0 and h[0] == h_del[0]:
        heapq.heappop(h)
        sz[0] -= 1
        heapq.heappop(h_del)
        sz_del[0] -= 1
    if sz[0] != 0:
        sys.stdout.write(str(heapq.nsmallest(1, h)[0])+'\n')
    else:
        sys.stdout.write(str(-1)+'\n')

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
            heapq.heappush(h, x)
            sz_h[0]+=1
            new_getMin(h,sz_h, h_del, sz_del)
            #print(Q)
        else:
            x = Q.popleft()
            #print(Q)
            heapq.heappush(h_del, x)
            sz_del[0] += 1
            new_getMin(h, sz_h, h_del, sz_del)
            #print(h_del)

if __name__ == '__main__':
    main()
