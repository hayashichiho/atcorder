N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# prev[i] は 部屋 i に到達する直前の部屋の番号
dp = [0] * (N + 1)
prev = [0] * (N + 1)

dp[1] = 0
prev[1] = 1

dp[2] = dp[1] + A[0]
prev[2] = 1

# 部屋3から部屋Nまでの動的計画法
for i in range(3, N + 1):
    cost_from_i_minus_1 = dp[i - 1] + A[i - 2]  # 部屋 i-1 から部屋 i へのコスト
    cost_from_i_minus_2 = dp[i - 2] + B[i - 3]  # 部屋 i-2 から部屋 i へのコスト

    if cost_from_i_minus_1 <= cost_from_i_minus_2:
        dp[i] = cost_from_i_minus_1
        prev[i] = i - 1
    else:
        dp[i] = cost_from_i_minus_2
        prev[i] = i - 2

# 経路復元
path = []
curr_room = N
while curr_room != 1:
    path.append(curr_room)
    curr_room = prev[curr_room]
path.append(1)
path.reverse()

# 結果出力
print(len(path))
print(*path)
