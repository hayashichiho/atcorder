N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = set(a + b for a in A for b in B)
CD = set(c + d for c in C for d in D)

for cd in CD:
    if (K - cd) in AB:
        print("Yes")
        break
else:
    print("No")
