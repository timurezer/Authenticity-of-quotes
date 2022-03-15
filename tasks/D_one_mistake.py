def z_foo(s, n):
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        k = max(min(z[i-l], r-i), 0)
        while i + k < n and s[i + k] == s[k]:
            k += 1
        z[i] = k
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z


def main():
    s = input()
    t = input()
    n, m = len(s), len(t)
    z1 = z_foo(s+'$'+t, n + m + 1)
    z2 = z_foo(s[::-1]+'$'+t[::-1], n + m + 1)
    res = []
    for i in range(n + 1, m + 2):
        if z1[i] == n:
            res.append(i - n)
        elif z2[m + n + 1 - i + 1] == n - z1[i] - 1:
            res.append(i - n)
    print(len(res))
    print(*res)

main()

'''
aba
abacaba

'''
