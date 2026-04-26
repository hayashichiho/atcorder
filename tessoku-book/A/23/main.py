from itertools import combinations


def solve():
    N, M = map(int, input().split())

    # 各クーポン券が無料で買える品物のセットをビットで表現
    coupons = []
    for _ in range(M):
        items = list(map(int, input().split()))
        coupon_bits = 0
        for j in range(N):
            if items[j] == 1:
                coupon_bits |= 1 << j
        coupons.append(coupon_bits)

    # 必要な品物すべてのビットが立った状態
    all_items = (1 << N) - 1

    # 1枚からM枚まで、クーポン券の組み合わせを試す
    for num_coupons in range(1, M + 1):
        for combo in combinations(coupons, num_coupons):
            current_items = 0
            for coupon in combo:
                current_items |= coupon

            # すべての品物を買えたかチェック
            if current_items == all_items:
                print(num_coupons)
                return

    # すべて試しても見つからなかった場合
    print(-1)


if __name__ == "__main__":
    solve()
