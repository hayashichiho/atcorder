N = int(input())

# 3で割り切れる数の個数
count_3 = N // 3

# 5で割り切れる数の個数
count_5 = N // 5

# 15で割り切れる数の個数（重複分）
count_15 = N // 15

# 包除原理を使って最終的な個数を計算
result = count_3 + count_5 - count_15

print(result)
