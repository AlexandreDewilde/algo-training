#based on jury slides for k=10
n = int(input())


a = input()
b = input()

def lcs(s1, s2):
    dp = [[""]*(len(s2)+1) for _ in range(len(s1)+1)]

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                continue
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + s1[i-1]
            elif len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[len(s1)][len(s2)]

ans = []
for i in range(0,n-10, 10):
    ans.append(lcs(a[i:i+10], b[i:i+10]))

print("".join(ans))