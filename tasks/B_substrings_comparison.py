def hash(s):
    n = len(s)
    h = [0] * (n + 1)
    deg = [1] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i-1] * x + ord(s[i-1])) % m
        deg[i] = (deg[i-1] * x) % m
    return h, deg


def get_hash(l, r):
    # return hash of s[l, r)
    return (h[r] - h[l] * deg[r - l]) % m

def query(l1, r1, l2, r2):
    # print('s1:', s1)
    # print('s2:', s2)
    left, right = -1, min(r1 - l1, r2 - l2) - 1    # это относительные индексы, правая граница включается (n-1)
    # print("left, right:", left, right)
    while right - left > 1:
        m = (left + right) // 2
        # print("m", m)
        h1 = get_hash(l1, l1 + m + 1)     # получили hash of s[l1, l1 + m]
        h2 = get_hash(l2, l2 + m + 1)
        if h1 == h2:
            left = m
            # print("left", left)
        else:
            right = m
            # print("right", right)
    h1 = get_hash(l1, l1 + right + 1)
    h2 = get_hash(l2, l2 + right + 1)
    if h1 == h2:
        if r1 - l1 < r2 - l2:
            return '<'
        elif r1 - l1 > r2 - l2:
            return '>'
        else:
            return '='
    else:
        # print('not equal hashes')
        # print('s1:', s1[:right + 1])
        # print('s2:', s2[:right + 1])
        if ord(s[l1 + right]) < ord(s[l2 + right]):    # сравниваем первое отличие в строках
            return '<'
        else:
            return '>'


def main():
    global s, h, deg, x, m
    m = 27644437
    x = 256
    s = input()
    q = int(input())
    h, deg = hash(s)
    for _ in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        print(query(l1 - 1, r1, l2 - 1, r2))
        # print()

if __name__ == "__main__":
    main()
