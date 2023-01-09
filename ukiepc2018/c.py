import sys

input = sys.stdin.readline

r, c = map(int, input().split())
l = int(input())

dp = [[1]*c for _ in range(r)]
mod = int(1e9) + 7

total = 1
for step in range(l-1):
    total = sum(map(sum, dp))
    new_dp = [[total]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if 0<=i+dx < r and 0<=j+dy < c:
                        new_dp[i+dx][j+dy] -= dp[i][j]
                        new_dp[i+dx][j+dy] %= mod
    dp = new_dp


tot = 0
for row in dp:
    for el in row:
        tot += el
        tot %= mod

print((tot)%mod)