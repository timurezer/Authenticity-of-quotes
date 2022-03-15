def z_foo(s, n):
    z = [0] * n
    r, l = 0, 0
    for i in range(n):      # !!!!!!11
        print(l, r)
        k = max(min(z[i-l], r-i), 0)
        while i + k < n and s[i + k] == s[k]:
            k += 1
        z[i] = k
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z


# def main():
#     a = input()
#     b = input()
#     m, n = len(a), len(b)
#     z = z_foo(b+'$'+a, n + m + 1)
#     res = []
#     for i in range(n + 1, m + n + 1):
#         if z[i] == n:
#             res.append(i - n)
#     print(len(res))
#     print(' '.join(map(str, res)))
#
# main()

def main():
    s = input()
    z = z_foo(s, len(s))
    print(z)

main()
