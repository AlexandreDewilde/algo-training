h, w = map(int, input().split())

mod = int(1e9) + 7
grid = [list(input()) for _ in range(h)]

dp = [[0] * w for _ in range(h)]

dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            continue
        dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % mod
        dp[i][j] %= mod

print(dp[h - 1][w - 1])