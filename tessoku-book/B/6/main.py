N = int(input())
A = list(map(int, input().split()))
Q = int(input())
score = [0] * (N + 1)
for i in range(N):
    if A[i] == 0:
        A[i] = -1

for i in range(1, N + 1):
    score[i] = score[i - 1] + A[i - 1]

for _ in range(Q):
    L, R = map(int, input().split())
    re_score = score[R] - score[L - 1]
    if re_score > 0:
        print("win")
    elif re_score == 0:
        print("draw")
    else:
        print("lose")
