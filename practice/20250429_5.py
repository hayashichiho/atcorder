def divisor(num): # 約数の個数を返してくれる関数

    ret = 0
    for i in range(1, num+1):
        if(num%i == 0): ret += 1

    return ret

n = int(input())

if(n <= 105): # 出力例1 に「ただ一つ」というヒントがあるので大人しく従います。
    if(n==105): print(1)
    else: print(0)
    exit()

res = 1
for i in range(106, n+1):
    if(divisor(i) == 8 and i%2==1): res += 1 # 「約数の個数がちょうど8の奇数」をそのまま実装

print(res)
