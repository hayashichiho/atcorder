S = input()
T = input()
len_s = len(S)
len_t = len(T)

# dp[i][j] を、Sのi文字目までとTのj文字目までの最長共通部分列の長さとする
dp = [[0] * (len_t + 1) for _ in range(len_s + 1)]

# 動的計画法
for i in range(1, len_s + 1):
    for j in range(1, len_t + 1):
        if S[i - 1] == T[j - 1]:
            # 文字が一致する場合
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # 文字が一致しない場合
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len_s][len_t])
