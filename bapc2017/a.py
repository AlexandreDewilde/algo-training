import math
n, m, r = input().split()
n = int(n)
m = int(m)
r = float(r)

ax,ay,bx,by = map(int, input().split())

ans = r / m * ay + r / m * by

rad = min(r / m * ay, r / m * by)
ans = min(ans, r/m*abs(ay-by)+2*rad*math.pi*abs(bx-ax)/(2*n))
print(ans)

