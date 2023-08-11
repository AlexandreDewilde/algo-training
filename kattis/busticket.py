s, p, m, n = map(int, input().split())

t = [0] + list(map(int, input().split()))


current = 1
dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    while t[i] - t[current] >= m:
        current += 1
    dp[i] = min(dp[i], dp[i - 1] + min(s, p), dp[current - 1] + p)
# print(dp)
print(dp[n])