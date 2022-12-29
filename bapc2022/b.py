import math

n = int(input())

coords = []
for _ in range(n):
    x,y = map(int, input().split())
    coords.append((x,y))

ans = 0
for x,y in coords:
    if coords[0] != (x,y):
        angle = math.atan((y-coords[0][1])/(x-coords[0][0]))
        ans = max(ans, math.degrees(angle))
    if (x,y) != coords[-1]:
        angle = -math.atan((coords[-1][1]-y)/(coords[-1][0]-x))
        ans = max(ans, math.degrees(angle))

print(ans)