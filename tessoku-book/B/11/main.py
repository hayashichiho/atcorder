from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(A)

Q = int(input())
for _ in range(Q):
    x = int(input())
    print(bisect_left(A_sorted, x))
