H, W, N = map(int, input().split())
sum = [[0] * (W + 1) for _ in range(H + 1)]

for n in range(N):
    A, B, C, D = map(int, input().split())
    sum[A][B] += 1
    sum[A][D + 1] -= 1
    sum[C + 1][B] -= 1
    sum[C + 1][D + 1] += 1

for h in range(1, H + 1):
    for w in range(1, W + 1):
        sum[h][w] += sum[h][w - 1]

for w in range(1, W + 1):
    for h in range(1, H + 1):
        sum[h][w] += sum[h - 1][w]

for h in range(1, H + 1):
    print(*sum[h][1 : W + 1])
