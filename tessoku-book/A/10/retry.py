N = int(input())
A = list(map(int, input().split()))

D = int(input())

left_maxroom = [0] * N
right_maxroom = [0] * N

for i in range(N):
    left_maxroom[i] = max(left_maxroom[i - 1], A[i]) if i - 1 >= 0 else A[i]
    right_maxroom[N - 1 - i] = max(right_maxroom[N - i], A[N - 1 - i]) if N - i < N else A[N - 1 - i]

for d in range(D):
    L, R = map(int, input().split())
    left = left_maxroom[L - 2] if L - 2 >= 0 else -1
    right = right_maxroom[R] if R < N else -1
    print(max(left, right))
