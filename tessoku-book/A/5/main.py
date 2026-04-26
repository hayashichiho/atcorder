N, K = map(int, input().split())
count = 0
for red in range(1, N + 1):
    for blue in range(1, N + 1):
        white = K - red - blue
        if 1 <= white <= N:
            count += 1
print(count)
