def hash(s):
    h = [0] * (n + 1)
    deg = [1] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i-1] * x + ord(s[i-1])) % m
        deg[i] = (deg[i-1] * x) % m
    return h, deg

def get_hash(l, r, h):
    # return hash of s[l, r)
    return (h[r] - h[l] * deg[r - l]) % m

def init_table():
    return [None] * (m + 1)

def common_search(l):
    table = init_table()    # создаем новую хэш таблицу
    for i in range(0, n - l + 1):
        id = get_hash(i, i + l, h1)
        # кладем не саму строку, а индекс, с которого эта подстрока начинается в исходной строке
        # проверять на коллизии не нужно, потому что подобрали большой размер таблицы (10^7, а всего слов 10^5)
        table[id] = i
    for i in range(0, n - l + 1):
        id = get_hash(i, i + l, h2)
        x = table[id]
        if x is not None and s1[x:x+l] == s2[i:i+l]:    # хэши могли совпасть случайно, поэтому чекаем что это такая же строка
            return s2[i:i+l]
    return None

def bin_common_search():
    left, right = 0, n + 1
    res = ''
    while right - left > 1:
        m = (left + right)//2
        cur_res = common_search(m)
        if cur_res is not None:
            res = cur_res
            left = m
        else:
            right = m
    return res


def main():
    global deg, x, m, n, s1, s2, h1, h2
    x = 256
    m = 16769023
    n = int(input())
    s1, s2 = input(), input()
    h1, deg = hash(s1)
    h2, deg = hash(s2)
    res = bin_common_search()
    print(res)


if __name__ == '__main__':
    main()
