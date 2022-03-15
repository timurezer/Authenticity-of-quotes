import sys

def search(n, s):
    d = [1]*n   # list of lengths
    p = [None]*n    # list of privios elements
    for i in range(n):
        for j in range(i):
            if s[j] < s[i]:
                if d[i] < d[j] + 1:
                    p[i] = j
                    d[i] = d[j] + 1
    return d, p



def recover(n, d, p, s):
    max_ind = 0
    max_len = -1
    for i in range(n):
        if d[i] > max_len:
            max_len = d[i]
            max_ind = i
    ans = [None]*(d[max_ind])
    cur = max_ind
    for i in range(d[max_ind]):
        ans[i] = s[cur]
        cur = p[cur]
    return d[max_ind], ans[::-1]

def main():
    n = int(input())
    s = list(map(int, sys.stdin.readline().split()))
    d, p = search(n, s)
    max_len, ans = recover(n, d, p, s)
    sys.stdout.write(str(max_len)+'\n')
    sys.stdout.write(' '.join(map(str, ans))+'\n')

if __name__ == '__main__':
    main()
