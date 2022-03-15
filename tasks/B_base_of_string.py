def z_foo(s, n):
    z = [0] * n
    r, l = 0, 0
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
    a = input()
    n = len(a)
    z = z_foo(a, n)
    flag = True
    for i in range(n):
        if z[i] == n-i:
            print(i)
            flag = False
            break
    if flag:
        print(n)

main()
