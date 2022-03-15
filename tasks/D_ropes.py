def check(ropes, k, m):
    k_curr = 0
    for l in ropes:
        k_curr += l // m
    if k_curr >= k:
        return True
    else:
        return False


def main():
    n, k = map(int, input().split())
    ropes = []
    total_length = 0
    for i in range(n):
        x = int(input())
        total_length += x
        ropes.append(x)
    #print(ropes)
    left = 1
    right = total_length//k + 1
    if right == 1:
        print(0)
    else:
        while right - left > 1:
            m = (left + right)//2
            if check(ropes, k, m): left = m
            else: right = m
        print(left)


if __name__ == '__main__':
    main()

'''
3 5
2 
4 
5
'''
