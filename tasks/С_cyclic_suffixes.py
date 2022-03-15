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
    n = len(s)
    pos_acc = 1
    z = z_foo(s, n)
    for i in range(1, n):
        if s[z[i]] > s[(i + z[i]) % n]:
            pos_acc += 1
        elif i + z[i] == n:
            j = z[i]
            if j + z[j] < n and s[j + z[j]] > s[z[j]]:
                pos_acc += 1

    print(pos_acc)

main()
