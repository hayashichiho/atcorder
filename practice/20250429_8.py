a,b,c,x,y = map(int, input().split())

res = a * x + b * y

for i in range(1, max(x, y) + 1):
    ab = i * 2
    cand = ab*c + a*max(0,x-1) + b*max(0,y-1)

    res = min(res, cand)

print(res)
