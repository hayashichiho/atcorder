N = int(input())
A = [int (i) for i  in input().split()]
ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += A[i]
print(ans)
