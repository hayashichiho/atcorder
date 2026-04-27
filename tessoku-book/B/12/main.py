N = int(input())


def f(x):
    return x**3 + x - N


left = 0
right = N

while right - left > 0.001:
    mid = (left + right) / 2
    if f(mid) > 0:
        right = mid
    else:
        left = mid
print("%.6f" % mid)
