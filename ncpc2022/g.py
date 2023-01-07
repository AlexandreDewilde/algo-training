n,k = map(int, input().split())

p = list(map(float, input().split()))

p.sort(reverse=True)

dp = [0]*(2*n+10)
dp[0] = 1
ans = 0
for it in range(n):
    new_dp = [0]*len(dp)
    score = 0
    for i in range(-n, n+1):
        new_dp[i] = dp[i-1]*p[it] + dp[i+1]*(1-p[it])
        if i >= k:
            score += new_dp[i]
    dp = new_dp
    ans = max(ans, score)

print(ans)