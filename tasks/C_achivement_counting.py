# def get(v):     # old get
#     if v == p[v]:
#         return v
#     old_p = p[v]
#     d[v] += d[p[v]]
#     p[v] = get(p[v])
#     if old_p == p[v]:
#         d[v] -= d[p[v]]
#     return p[v]

def get(v):     # old get
    if v == p[v]:
        return v
    old_p = p[v]
    p[v] = get(p[v])
    x = get_points(old_p)
    d[v] = (d[v] + x) - d[p[v]]
    # if old_p == p[v]:
    #     d[v] -= d[p[v]]
    return p[v]

def get_points(v):
    if v == p[v]:
        return d[v]
    else:
        return d[v] + d[p[v]]

def join(v, u):
    a, b = get(v), get(u)
    if r[b] > r[a]:
        a, b = b, a
    p[b] = a
    if r[a] == r[b]:
        r[a] += 1
    d[b] -= d[a]

def add(v, x):
    root = get(v)
    d[root] += x


def main():
    global n, p, r, d
    n, m = map(int, input().split())
    p = [i for i in range(n + 1)]
    r = [1] * (n + 1)
    d = [0] * (n + 1)
    for _ in range(m):
        lst = list(input().split())
        if lst[0] == 'add':
            add(int(lst[1]), int(lst[2]))
        elif lst[0] == 'join':
            join(int(lst[1]), int(lst[2]))
            print('p', p)
            print('d', d)
            print()
        else:
            get(int(lst[1]))
            print('p', p)
            print('d', d)
            print(get_points(int(lst[1])))
            print()

# main()

p = [0, 1, 1, 2, 3, 4]
d = [0, 1, 2, 3, 4, 5]


get(5)
print('p', p)
print('d', d)
# get_points(1)
# get_points(2)
# get_points(3)
print(get_points(5))


'''
4 8
add 1 10
add 2 15
add 3 5
add 4 3
join 1 2
join 3 4
join 2 4
get 4

'''

'''
5 10
add 1 1
add 2 2
add 3 3
add 4 4
add 5 5
join 2 3
join 4 5
join 1 5
join 3 1
get 3
'''

'''
10 20
add 1 1
add 2 2
add 3 3
add 4 4
add 5 5
add 6 6
add 7 7
add 8 8
add 9 9
add 10 10
join 2 3
join 4 5
join 1 5
join 3 1
join 7 8
join 9 10
join 6 10
join 8 6
join 9 4
get 5
'''
