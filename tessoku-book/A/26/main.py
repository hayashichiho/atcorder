def sieve(n):
    """
    エラトステネスのふるいを用いて、nまでの素数判定テーブルを作成する
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def solve():
    Q = int(input())
    queries = [int(input()) for _ in range(Q)]

    max_x = max(queries)

    # 判定に必要な最大値までの素数テーブルを事前に作成
    is_prime_table = sieve(max_x)

    for x in queries:
        if is_prime_table[x]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
