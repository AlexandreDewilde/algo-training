n = int(input())

# Derangements formula
k = 1
ans = 0
for i in range(n+1):
    if 1/k < 1e-20:
        break
    if i > 0:
        k *= i
    if i % 2 == 0:
        ans += 1/k
    else:
        ans -= 1/k

print(1-ans)