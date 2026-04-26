N, W = map(int, input().split())

items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

# dp[w] = 重さwにおける最大価値
dp = [0] * (W + 1)

# 動的計画法
for w_i, v_i in items:
    for w in range(W, w_i - 1, -1):
        dp[w] = max(dp[w], dp[w - w_i] + v_i)  # dp[w - w_i] + v_iは、重さw_iの品物を選んだ場合の価値

print(dp[W])
