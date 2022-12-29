n = int(input())
p = list(map(int, input().split()))


dp = [float("-inf") for _ in range(n)]
dp[0] = p[0]

for k in range(n-1, 0, -1):
    for i in range(n):
        if i+k >= n:
            break
        dp[i+k] = max(dp[i+k], dp[i]+p[i+k])
print(dp[-1])