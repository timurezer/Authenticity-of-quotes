def hash(s):
    n = len(s)
    h = [0] * (n + 1)
    deg = [1] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i-1] * x + ord(s[i-1])) % m
        deg[i] = (deg[i-1] * x) % m
    return h, deg


def get_hash(l, r):
    return (h[r] - h[l]* deg[r - l]) % m

def main():
    global m, x, h, deg, s
    m = 27644437
    x = 256
    s = input()
    h, deg = hash(s)
    q = int(input())
    res = []
    for i in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        if get_hash(l1 - 1, r1) == get_hash(l2 - 1, r2):
            res.append('+')
        else:
            res.append('-')
    print(''.join(map(str, res)))

main()
