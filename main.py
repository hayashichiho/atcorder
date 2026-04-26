from typing import List


def is_valid_layout(n: int, k: int, buildings: List[List[int]]) -> bool:
    for r in range(n - 1):
        for c in range(n - 1):
            count = buildings[r][c] + buildings[r + 1][c] + buildings[r][c + 1] + buildings[r + 1][c + 1]
            if count > k:
                return False

    return True


def main() -> None:
    n, m, k = map(int, input().split())
    buildings = [[0] * n for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        i, j = a - 1, b - 1
        buildings[i][j] = 1

    print("yes" if is_valid_layout(n, k, buildings) else "no")


if __name__ == "__main__":
    main()
