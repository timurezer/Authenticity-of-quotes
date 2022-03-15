import sys
from collections import deque

def pushh(s, x):
    if s == []:
        s.append([x,x])
    else:
        y = s[-1][1]
        if y < x: s.append([x, y])
        else: s.append([x, x])

def getMin(s):
    if s == []: return -1
    else: return s[-1][1]

def getMinQ(s1, s2):
    x = getMin(s1)
    y = getMin(s2)
    if x == -1 or y == -1:
        return max(x, y)
    else:
        return min(x, y)

def main():
    q = int(sys.stdin.readline())
    s1 = []
    s2 = []
    for i in range(q):
        a = str(sys.stdin.readline())
        if a[0] == '+':
            x = int(a[2:])
            pushh(s1, x)
            sys.stdout.write(str(getMinQ(s1, s2))+'\n')
        else:
            if s2 == []:
                for x in s1[::-1]:
                    pushh(s2, x[0])
                s1 = []
            del s2[-1]
            sys.stdout.write(str(getMinQ(s1, s2))+'\n')

if __name__ == '__main__':
    main()

'''
10
+ 1
+ 2
+ 3
+ 4
+ 5
-
-
-
-
-
'''
'''
10
+ 1
+ 2
+ 3
-
-
+ 4
+ 5
-
-
-
'''
'''
10
+ 1
-
+ 3
-
+ 2
-
+ 4
-
+ 5
-
'''
