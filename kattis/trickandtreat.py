n, m = map(int, input().split())

k = list(map(int, input().split()))


l = 1
r = m

def eval(x):
    ans = 0
    for el in k:
        if el <= x: x -= el
        else: ans += 1
    return ans

best = float("inf")
for i in range(max(0, m - 45), m+1):
    best = min(best, eval(i))

print(best)