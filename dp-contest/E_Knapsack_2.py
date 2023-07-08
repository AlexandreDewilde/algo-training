n, w = map(int, input().split())

items = []
for _ in range(n):
    items.append(tuple(map(int, input().split())))
    
m = sum(item[1] for item in items)
dp = [float("inf")] * (m + 1)
dp[0] = 0

for ww, v in items:
    for i in range(m, -1, -1):
        if i + v > m:
            continue
        dp[i + v] = min(dp[i + v], dp[i] + ww)

print(max((i for i in range(m+1) if dp[i] <= w)))