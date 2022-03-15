from collections import deque

def pop(q: list):
    x = q[-1]
    del q[-1]
    return x

def push(q: list, x):
    q.append(x)

def oper(a: str, b: str, c: str):
    if a == '+':
        return str(int(b) + int(c))
    elif a == '-': return str(-int(b) + int(c))
    else: return str(int(b) * int(c))

def count(s):
    opers = ('+', '-', '*')
    q1 = deque(s[::-1])
    print(q1)
    q2 = deque([])
    q3 = deque([])
    while q1 != q3:
        x = q1.popleft()
        if x not in opers:
            q2.append(x)
        else:
            y = q2.pop()
            z = q2.pop()
            q2.append(oper(x, y, z))
    return q2.pop()

def main():
    s = [str(x) for x in input().split()]
    print(count(s))

if __name__ == '__main__':
    main()
