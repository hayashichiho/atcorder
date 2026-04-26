H, W = map(int, input().split())

X = [0] * (H + 1)
for i in range(1, H + 1):
    X[i] = [0] + list(map(int, input().split()))

sum = [[0] * (W + 1) for _ in range(H + 1)]

for h in range(1, H + 1):
    for w in range(1, W + 1):
        sum[h][w] = sum[h - 1][w] + sum[h][w - 1] + X[h][w] - sum[h - 1][w - 1]

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(sum[C][D] - sum[A - 1][D] - sum[C][B - 1] + sum[A - 1][B - 1])
