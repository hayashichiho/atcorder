n, r = map(int, input().split())
MOD = 1000000007


# 階乗を計算する関数
def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result = (result * i) % MOD
    return result


def combination(n, r):
    if r > n:
        return 0
    return (factorial(n) * pow(factorial(r), MOD - 2, MOD) * pow(factorial(n - r), MOD - 2, MOD)) % MOD


print(combination(n, r))
