def solve():
    N = int(input())
    MOD = 10000
    current_number = 0

    for _ in range(N):
        op, A = input().split()
        A = int(A)

        if op == "+":
            current_number += A
        elif op == "-":
            current_number -= A
        elif op == "*":
            current_number *= A

        current_number %= MOD
        print(current_number)


if __name__ == "__main__":
    solve()
