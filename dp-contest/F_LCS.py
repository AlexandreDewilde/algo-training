s = input()
t = input()

dp = [[0]*len(t) for _ in range(len(s))]

for i in range(len(s)):
    for j in range(len(t)):
        prev = dp[i-1][j-1] if i and j else 0
        if s[i] == t[j]:
            dp[i][j] = max(prev + 1, dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
ans = ""
n = dp[len(s) - 1][len(t) - 1]
i = len(s) - 1
j = len(t) - 1
while n:
    if s[i] == t[j]:
        ans += s[i]
        i -= 1
        j -= 1
        n -= 1
    elif i > 0 and dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1

print(ans[::-1])