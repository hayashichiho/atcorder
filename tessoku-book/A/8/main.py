H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

S = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j] + X[i][j]

Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    ans = S[C][D] - S[A - 1][D] - S[C][B - 1] + S[A - 1][B - 1]
    print(ans)
