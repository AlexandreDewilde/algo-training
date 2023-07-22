x, y, q, r, x2, y2, q2, r2 = map(int, input().split())

d1 = ((x - q)**2 + (y - r)**2)**0.5
d2 = ((x2-q2)**2 + (y2-r2)**2)**0.5
print(max(d1, d2))