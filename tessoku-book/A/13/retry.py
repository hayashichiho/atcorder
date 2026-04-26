N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
right = 1

for left in range(N):
    while right < N and A[right] - A[left] <= K:
        right += 1
    ans += right - left - 1
print(ans)
