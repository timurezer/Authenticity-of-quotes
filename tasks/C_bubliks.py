import sys

def nickelback(n, w, v):
    v.sort(reverse= True)
    res = ''
    i = 0
    numb = 0
    while w != 0:
        k = w // v[i]
        res += k*(str(v[i])+' ')
        numb += k
        w = w % v[i]
        i += 1
    return str(numb), res


def main():
    n, w = map(int, sys.stdin.readline().split())
    v = list(map(int, sys.stdin.readline().split()))
    m, res = nickelback(n, w, v)
    sys.stdout.write(m+'\n'+res)

if __name__ == '__main__':
    main()
