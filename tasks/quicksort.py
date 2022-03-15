from random import randint, uniform


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def Partition(a, l, r):     # this partition may meet pivot and go next
    x = a[randint(l, r)]
    #print('x=', x)
    i, j = l, r
    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            swap(a, i, j)
            i += 1
            j -= 1
    return i, j     # this indexes do not contain pivot


def qsort(a, l, r):
    if r - l <= 0:
        print('l, r=', l, r, '\n' + str(a[l:r+1]))
        print('end')
        return
    print('l, r=', l, r, '\n' + str(a))
    i, j = Partition(a, l, r)
    print('i, j=', i, j, '\n'+str(a)+'\n')
    qsort(a, l, j)
    qsort(a, i, r)


def main2():
    N = 1000
    for i in range(N):
        n = 1000
        s1 = [randint(0, 10) for i in range(n)]
        #s1 = [6,5]
        s2 = [x for x in s1]
        qsort(s1, 0, n-1)
        s2 = sorted(s2, reverse= False)
        #print(s1)
        #print(s2)
        if s1 != s2:
            print(i, 'No')


def main1():
    n = 10
    s1 = [randint(0, 5) for i in range(n)]
    print(s1)
    qsort(s1, 0, n-1)
    print(s1)

def main():
    s = [8, 20, 11, 1, 30]
    qsort(s, 0, 4)
    print(s)

if __name__ == '__main__':
    main()
