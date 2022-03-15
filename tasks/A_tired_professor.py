import sys
from collections import deque

def tired_count(s: deque, n, m):
    x = s[0]
    y = s[-1]
    if x < y:
        s.popleft()
        s.append((x + y) % m)
    else:
        s.pop()
        s.appendleft((y - x) % m)

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = deque(list(map(int, sys.stdin.readline().split())))
    m = 2**30
    for i in range(k):
        tired_count(s, n, m)
        #print(s)
    sys.stdout.write(' '.join(map(str, s)))

if __name__ == '__main__':
    main()
