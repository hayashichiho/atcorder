# 英語を格納
S = set(input())  # 入力をそのままセットに変換

# aからzまでの文字を格納
a = [chr(i) for i in range(97, 123)]

# S に含まれない英小文字を探す
for char in a:
    if char not in S:
        print(char)
        break
