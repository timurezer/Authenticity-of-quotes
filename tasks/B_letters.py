def main():
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = tuple(map(int, input().split()))
    for i in range(2, n+1):
        a[i] += a[i-1]
    a = tuple(a)
    i = 1   # number of dorminostory - 1
    for x in b:
        flag = False    # еще не нашли комнату
        while flag != True:
            if x <= a[i]:
                print(i, x - a[i-1])
                flag = True
            else:
                i += 1

if __name__ == '__main__':
    main()
