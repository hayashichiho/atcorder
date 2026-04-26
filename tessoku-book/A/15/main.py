N = int(input())
A = list(map(int, input().split()))

sorted_unique = sorted(set(A))
rank = {x: i + 1 for i, x in enumerate(sorted_unique)}

B = [rank[x] for x in A]
print(*B)
