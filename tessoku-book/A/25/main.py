def solve():
    H, W = map(int, input().split())
    grid = [input().strip() for _ in range(H)]

    # dp[i][j] = マス(1,1)からマス(i,j)への経路の総数
    dp = [[0] * W for _ in range(H)]

    # スタート地点の初期化
    if grid[0][0] == ".":
        dp[0][0] = 1

    # DPテーブルを埋める
    for i in range(H):
        for j in range(W):
            # 黒いマスはスキップ
            if grid[i][j] == "#":
                continue

            # 上からの移動
            if i > 0 and grid[i - 1][j] == ".":
                dp[i][j] += dp[i - 1][j]

            # 左からの移動
            if j > 0 and grid[i][j - 1] == ".":
                dp[i][j] += dp[i][j - 1]

    print(dp[H - 1][W - 1])


if __name__ == "__main__":
    solve()
