N = int(input())
points = []
max_coordinate = 0

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    max_coordinate = max(max_coordinate, x, y)

Q = int(input())
queries = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    queries.append((a, b, c, d))
    max_coordinate = max(max_coordinate, c, d)

size = max_coordinate + 2
prefix = [[0] * size for _ in range(size)]

for x, y in points:
    prefix[x + 1][y + 1] += 1

for i in range(1, size):
    for j in range(1, size):
        prefix[i][j] += prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1]

for a, b, c, d in queries:
    a += 1
    b += 1
    c += 1
    d += 1
    ans = prefix[c][d] - prefix[a - 1][d] - prefix[c][b - 1] + prefix[a - 1][b - 1]
    print(ans)
