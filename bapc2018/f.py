import math

n, m = map(int, input().split())

l = []
for i in range(n):
    p, c = map(int, input().split())
    l.append((p/c, p, c))
l.sort(reverse=True)

ans = float("inf")
cost = m
won = 0
for _, p, c in l:
    cost += c
    won += p
    ans = min(ans, math.ceil(cost/won))

print(ans)