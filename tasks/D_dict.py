class Node:
    def __init__(self):
        self.next = [None] * 26
        self.value = False

def add(s, i):
    cur = root
    for c in s:
        c = ord(c)-97
        if cur.next[c] is None:
            cur.next[c] = Node()
        cur = cur.next[c]
    cur.value = i

def get(s):
    cur= root
    for c in s:
        print(c)
        c = ord(c)-97
        print(cur.value)
        if cur.next[c] is None:
            return False
        cur = cur.next[c]
    return cur.value

def main():
    global root

    t = input()
    q = int(input())
    d = []
    minlen = 10000000
    for _ in range(q):
        s = input()
        d.append(s)
        minlen = min(len(s), minlen)
    res = ['No'] * q
    root = Node()
    for i in range(q):
        add(d[i], i)
    for i in range(len(t) - minlen):
        print(t[i:])
        cur_check = get(t[i:])
        if cur_check is not None:
            d[cur_check] = 'Yes'

    for x in res:
        print(x)

main()
