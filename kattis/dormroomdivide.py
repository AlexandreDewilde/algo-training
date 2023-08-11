n = int(input())


def area(p1, p2, p3):
    return  0.5 * abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))


pts = []
for _ in range(n):
    pts.append(tuple(map(float, input().split())))


tot = 0
for i in range(n-1):
    tot += area(pts[0], pts[i], pts[i + 1])
tot /= 2

current = 0
for i in range(n-1):
    res = area(pts[0], pts[i], pts[i + 1])
    if current + res >= tot:
        break
    current += res

# mid = 0.5
# mp = (mid * (pts[i][0] + pts[i+1][0]), mid * (pts[i][1] + pts[i+1][1]))
# if abs(current + area(pts[0], pts[i], mp) - tot) < 1e-6:
#     print(*mp)
#     exit()

l = 0
r = 1

it = 0
while True:
    mid = (l + r) / 2

    pt = (mid * pts[i][0] + (1-mid) * pts[i+1][0], mid * pts[i][1] + (1-mid) * pts[i+1][1])
    
    a = area(pts[0], pts[i], pt)
    if(abs((a+current) - tot) < 1e-6 or it > 10000):
        print(*pt)
        exit()
    if a + current < tot:
        r = mid
    else:
        l = mid
    it += 1
