n = int(input())
roots = []
for _ in range(n):
    a,b = map(int, input().split())
    start = (a - b ** 0.5)
    end = (a + b ** 0.5)
    roots.append((start, a, b, False))
    roots.append((end, a, b, True))

roots.sort()

def eval(a, b, c, x):
    return a * x * x * x / 3 + b * x *x / 2 + c * x

total_a = 0
total_b = 0
total_a2 = 0
current = 0
ans = 0
prev = 0
for coord, a, b, rem in roots:
    if current >= 2:
        ans += eval(-current, 2 * total_a, total_b - total_a2, coord) - eval(-current, 2 * total_a, total_b - total_a2, prev)
    prev= coord
    if rem:
        current -= 1
        total_a2 -= a * a
        total_a -= a
        total_b -= b
        continue
    if current == 1:
        start_integral = coord
    total_a += a
    total_b += b
    total_a2 += a * a
    current += 1
print(ans)