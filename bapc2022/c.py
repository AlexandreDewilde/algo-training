# partially based on the jury presentation
c,t,r = map(int, input().split())

p = float(input())

prob = [0]*(c+1)
for i in range(c):
    prob[i+1] = (prob[i]+1+p*r) / (1-p)

dp = prob[:]

for i in range(1, c+1):
    for k in range(i+1):
        dp[i] = min(dp[i], dp[k]+t+prob[i-k])

print(dp[c]+t)



