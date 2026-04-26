def solve():
    a, b = map(int, input().split())
    MOD = 1000000007

    ans = 1

    # べき乗の指数bが0になるまで繰り返す
    while b > 0:
        # bの最下位ビットが1の場合（bが奇数）
        if b % 2 == 1:
            ans = (ans * a) % MOD

        # aを自乗し、bを半分にする
        a = (a * a) % MOD
        b //= 2

    print(ans)


if __name__ == "__main__":
    solve()
