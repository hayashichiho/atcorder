N, K = map(int, input().split())
A = list(map(int, input().split()))

possible = 1
for a in A:
    possible |= possible << a

print("Yes" if (possible >> K) & 1 else "No")
