n = int(input())
L = [int(input()) for _ in range(n)]

best = 0
l = 0
r = sum(L)

for i in range(n):
    l += L[i] ** 2
    r -= L[i]
    best = max(best, l * r)

print(best)