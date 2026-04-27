N = int(input())
h = list(map(int, input().split()))
costs = [0] * (N + 1)
costs[1] = abs(h[1] - h[0])

for i in range(2, N):
    costs[i] = min(costs[i - 1] + abs(h[i] - h[i - 1]), costs[i - 2] + abs(h[i] - h[i - 2]))


print(costs[N - 1])
