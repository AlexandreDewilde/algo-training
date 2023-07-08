n, w = map(int, input().split())

items = []
for _ in range(n):
    ww, v = map(int, input().split())
    items.append((ww, v))


dp = [0] * (w + 1)


for ww, v in items:
    for i in range(w, -1, -1):
        if i - ww < 0:
            continue
        dp[i] = max(dp[i], dp[i - ww] + v)
print(dp[w])