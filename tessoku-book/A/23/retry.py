from itertools import combinations

N, M = map(int, input().split())

coupons = [0] * M


for m in range(M):
    coupons_bits = 0
    items = list(map(int, input().split()))
    for n in range(N):
        if items[n] == 1:
            coupons_bits |= 1 << n
    coupons[m] = coupons_bits

all_items = (1 << N) - 1

for num_coupons in range(1, M + 1):
    for combo in combinations(coupons, num_coupons):
        current_items = 0
        for coupon in combo:
            current_items |= coupon

        if current_items == all_items:
            print(num_coupons)
            exit()
else:
    print(-1)
