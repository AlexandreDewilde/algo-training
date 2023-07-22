from math import gcd


k = int(input())

ans = float("inf")

for i in range(k):
    y, c1, c2 = map(int, input().split())
    ans = min(ans, y + c1 * c2 // gcd(c1, c2))
print(ans)