import sys
import math
input = sys.stdin.readline

t = int(input())
b = int(input())

balls = []
for i in range(b):
    d, s = map(int, input().split())
    balls.append((s,d))

balls.sort()
ans = 0
for d, s in balls:
    p = 2*d*math.pi
    if p*s <=t:
        ans += s
        t -= p*s
        continue
    
    ans += t // p
    break
print(int(ans))
