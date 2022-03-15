import sys

def sections_search(n, s):
    s.sort(key= lambda x: x[1])
    res = 1
    cur_r = s[0][1]
    for i in range(1, n):
        next_l = s[i][0]
        if next_l >= cur_r:
            res += 1
            cur_r = s[i][1]
    return res

def main():
    n = int(sys.stdin.readline())
    s = [0]*n
    for i in range(n):
         s[i] = tuple(map(int, sys.stdin.readline().split()))
    res = sections_search(n, s)
    sys.stdout.write(str(res))


if __name__ == '__main__':
    main()
