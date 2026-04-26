N = int(input())
A = list(map(int, input().split()))

sorted = sorted(set(A))
rank = {x: i + 1 for i, x in enumerate(sorted)}

B = [rank[x] for x in A]
print(*B)
