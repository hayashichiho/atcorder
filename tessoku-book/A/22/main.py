N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

dp = [-1] * (N + 1)
dp[1] = 0

for i in range(1, N):
    if dp[i] == -1:
        continue

    a_next = A_list[i - 1]
    if dp[i] + 100 > dp[a_next]:
        dp[a_next] = dp[i] + 100

    b_next = B_list[i - 1]
    if dp[i] + 150 > dp[b_next]:
        dp[b_next] = dp[i] + 150

print(dp[N])
