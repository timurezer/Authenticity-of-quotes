import sys

def correct_brackets(s):
    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]  # ответ для префикса i..j
    d = {'(' : ')', '[' : ']', '{' : '}'}
    opening = '([{'
    closing = ')]}'
    for l in range(1, n):   # перебираем все длины префиксов
        for i in range(n - l):
            dp[i][i+l] = max(dp[i+1][i+l], dp[i][i+l-1])    # а если удалить левую или правую скобочку
            if s[i] in opening and s[i+l] in closing:
                for k in range(i, i + l):
                    x = dp[i][k] + dp[k+1][i+l]       # ловим последовательности типа (..){..}
                    dp[i][i+l] = max(dp[i][i+l], x)
            if s[i] in d and d[s[i]] == s[i+l]:    # если у нас соответсвующие друг другу скобочки типа (...)
                dp[i][i+l] = max(dp[i][i+l], dp[i+1][i+l-1] + 2)
    print(dp[0][n-1])

def main():
    s = input()
    correct_brackets(s)


if __name__ == "__main__":
    main()
