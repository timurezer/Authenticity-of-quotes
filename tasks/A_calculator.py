import sys

a = 9999999

# is not used
def calc_rec(k, dp):
    if dp[k] != None:
        return dp[k]
    a = 1000001
    if k >= 2:
        a = min(a, calc_rec(k-1, dp) + 1)
    if k % 3 == 0:
        a = min(a, calc_rec(k//3, dp) + 1)
    if k % 2 == 0:
        a = min(a, calc_rec(k//2, dp) + 1)
    dp[k] = a
    return dp[k]

def calc_iter(n, dp):
    for i in range(2, n+1):
        dp[i] = a
        if i >= 2:
            dp[i] = min(dp[i], dp[i-1] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

def recover(n, numb, dp, p):
    cur = n
    i = numb
    p[i] = n
    while i > 0:
        if cur >=2 and dp[cur] == dp[cur-1] + 1:
            cur -= 1
            p[i-1] = cur
        elif cur % 3 == 0 and dp[cur] == dp[cur//3] + 1:
            cur //= 3
            p[i-1] = cur
        else:
            cur //= 2
            p[i-1] = cur
        i -= 1

def main():
    n = int(input())
    dp = [None]*(n+1)
    dp[1] = 0
    calc_iter(n, dp)
    numb = dp[n]
    p = [None]*(numb + 1)
    recover(n, numb, dp, p)
    sys.stdout.write(str(numb)+'\n')
    #sys.stdout.write(' '.join(map(str, dp[1:]))+'\n')
    sys.stdout.write(' '.join(map(str, p)))
    print(p)

if __name__ == '__main__':
    main()

'''

10
3
1 3 9 10

10
3
1 2 4 5 10 
'''
