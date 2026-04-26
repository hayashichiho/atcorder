N, K = map(int, input().split())
A = list(map(int, input().split()))


def count(t):
    return sum(t // a for a in A)


left = 0
right = 10**9

while left < right:
    mid = (left + right) // 2
    if count(mid) < K:
        left = mid + 1
    else:
        right = mid
print(left)
