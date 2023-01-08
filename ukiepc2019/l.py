import sys

input = sys.stdin.readline

r = int(input())

s = list(map(int, input().split()))

dp = [[float("inf")]*(r+1) for _ in range(len(s))]

for i in range(len(s)):
    dp[i][0] = 0

for turn in range(1,r+1):
    for i in range(len(s)):
        start = int(i//(1<<turn))*(1<<turn)
        if i < start+(1<<(turn-1)):
            interval = (1<<(turn-1), 1<<turn)
        else:
            interval = (0, 1<<(turn-1))
        for j in range(*interval):
            cj = start + j
            cost = max(0, (s[cj]-s[i]))**2
            dp[i][turn] = min(dp[i][turn], dp[i][turn-1]+dp[cj][turn-1]+cost)

print(dp[0][r])