N = int(input())
A = list(map(int, input().split()))

TARGET = 1000

for i in range(N):
    rest = TARGET - A[i]
    seen = set()
    for j in range(i + 1, N):
        rest2 = rest - A[j]
        if rest2 in seen:
            print("Yes")
            exit()
        seen.add(A[j])

print("No")
