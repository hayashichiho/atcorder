import bisect


def solve():
    """
    最長増加部分列の長さを求める
    """
    N = int(input())
    A = list(map(int, input().split()))

    # LISの末尾の値を管理する配列
    dp = []

    for a in A:
        idx = bisect.bisect_left(dp, a)
        if idx == len(dp):
            dp.append(a)
        else:
            dp[idx] = a
    print(len(dp))


if __name__ == "__main__":
    solve()
