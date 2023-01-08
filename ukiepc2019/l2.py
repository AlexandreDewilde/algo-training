import sys

input = sys.stdin.readline

#based on jury solution 
r = int(input())

s = list(map(int, input().split()))

dp = [[float("inf")]*(r+1) for _ in range(len(s))]

for i in range(len(s)):
    dp[i][r] = 0

half = 1
for turn in range(r-1,-1,-1):
    for j in range(0,len(s),half*2):
        l, m, r = j, j+half, j+half*2
        for a in range(l, m):
            for b in range(m, r):
                dp[a][turn] = min(dp[a][turn], dp[a][turn+1]+dp[b][turn+1]+max(0, s[b]-s[a])**2)
                dp[b][turn] = min(dp[b][turn], dp[a][turn+1]+dp[b][turn+1]+max(0, s[a]-s[b])**2)

    half <<= 1

print(dp[0][0])