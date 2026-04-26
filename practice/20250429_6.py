s = input()
n = len(s)

res = 0

for i in range(n):
    for j in range(i, n):
        sub = s[i:j+1]

        flag = True
        for c in sub:
            if(c not in ['A','G','T','C']):
                flag = False

            if(flag):
                res = max(res,len(sub))

print(res)
