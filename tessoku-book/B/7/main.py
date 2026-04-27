T = int(input())
N = int(input())
human = [0] * (T + 1)
sum = 0

for i in range(N):
    L, R = map(int, input().split())
    human[L] += 1
    human[R] -= 1

for j in range(T):
    sum += human[j]
    print(sum)
