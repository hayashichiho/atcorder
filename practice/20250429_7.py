n, m = map(int, input().split())
a = [list(map(int ,input().split())) for _ in range(n)]

res = 0
for one in range(m):
    for two  in range(m):
        sum = 0

        for i in range(n):
            sum += max(a[i][one], a[i][two])

        res = max(res, sum)

print(res)
