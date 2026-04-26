N = int(input())
P = [0] * (N + 2)
A = [0] * (N + 2)
for i in range(1, N + 1):
    P[i], A[i] = map(int, input().split())

dp = [[0] * (N + 2) for _ in range(N + 2)]

for length in range(N, 0, -1):
    for l in range(1, N - length + 2):
        r = l + length - 1

        score_left = 0
        if l > 1 and l <= P[l - 1] <= r:
            score_left = A[l - 1]
        val_l = dp[l - 1][r] + score_left

        score_right = 0
        if r < N and l <= P[r + 1] <= r:
            score_right = A[r + 1]
        val_r = dp[l][r + 1] + score_right

        if l == 1:
            dp[l][r] = val_r
        elif r == N:
            dp[l][r] = val_l
        else:
            dp[l][r] = max(val_l, val_r)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, dp[i][i])

print(ans)
