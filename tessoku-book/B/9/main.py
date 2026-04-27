N = int(input())
rectangles = []
max_x = 0
max_y = 0

for _ in range(N):
    a, b, c, d = map(int, input().split())
    rectangles.append((a, b, c, d))
    if c > max_x:
        max_x = c
    if d > max_y:
        max_y = d

imos = [[0] * (max_y + 1) for _ in range(max_x + 1)]

for a, b, c, d in rectangles:
    imos[a][b] += 1
    imos[c][b] -= 1
    imos[a][d] -= 1
    imos[c][d] += 1

for x in range(max_x + 1):
    for y in range(1, max_y + 1):
        imos[x][y] += imos[x][y - 1]

for x in range(1, max_x + 1):
    for y in range(max_y + 1):
        imos[x][y] += imos[x - 1][y]

answer = 0
for x in range(max_x):
    for y in range(max_y):
        if imos[x][y] > 0:
            answer += 1

print(answer)
