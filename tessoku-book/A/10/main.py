N = int(input())
A = list(map(int, input().split()))
D = int(input())

L = []
R = []

for _ in range(D):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

left_maxroom = [0] * N
right_maxroom = [0] * N

left_maxroom[0] = A[0]
right_maxroom[N - 1] = A[N - 1]

for i in range(1, N):
    left_maxroom[i] = max(left_maxroom[i - 1], A[i])
    right_maxroom[N - 1 - i] = max(right_maxroom[N - i], A[N - 1 - i])

for i in range(D):
    l = L[i]
    r = R[i]
    left = left_maxroom[l - 2] if l - 2 >= 0 else -1
    right = right_maxroom[r] if r < N else -1
    print(max(left, right))
