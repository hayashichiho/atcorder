N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (S + 1)
dp[0] = True

for card_value in A:
    for j in range(S, card_value - 1, -1):
        if dp[j - card_value]:
            dp[j] = True

if dp[S]:
    print("Yes")
else:
    print("No")
