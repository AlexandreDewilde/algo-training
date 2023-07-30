a = list(map(int, input().split()))

sides = [4, 6, 8, 12, 20]

m, mx = sum(a), sum(x * y for x, y in zip(sides, a))

mid = (m + mx) / 2

res = sorted([i for i in range(m, mx+1)], key=lambda x: abs(x - mid))

print(*res)