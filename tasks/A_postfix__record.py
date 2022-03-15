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
    q1 = s[::-1]
    q2 = []
    while q1 != []:
        x = pop(q1)
        if x not in opers:
            push(q2, x)
        else:
            y = pop(q2)
            z = pop(q2)
            push(q2, oper(x, y, z))
    return pop(q2)

def main():
    s = [str(x) for x in input().split()]
    print(count(s))

if __name__ == '__main__':
    main()
