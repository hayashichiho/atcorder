N, K = map(int, input().split())
A = list(map(int, input().split()))
costs = [0] * (N + 1)
count = 0

for i in range(1, N + 1):
    costs[i] = costs[i - 1] + A[i - 1]

for j in range(1, N + 1):
    for k in range(j, N + 1):
        if costs[k] - costs[j - 1] <= K:
            count += 1
        else:
            break

print(count)
