D = int(input())
N = int(input())
attendance = [0] * (D + 1)

for _ in range(N):
    L, R = map(int, input().split())
    attendance[L - 1] += 1
    attendance[R] -= 1

for i in range(1, D):
    attendance[i] += attendance[i - 1]

for i in range(D):
    print(attendance[i])
