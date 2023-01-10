from math import gcd

n = int(input())

basements = []
H = 0
for i in range(n):
    h,r,t = map(int, input().split())
    basements.append((h,r,t))
    H = max(H, h)

can = [True]*1865*H
for h,r,t in basements:
    time = (t-r) % h - 1

    if time <= 0:
        continue
    if r > t:
        for j in range(t):
            can[j] = False
    for i in range(r, len(can), h):
        for j in range(i+1,min(time+i+1,len(can))):
            can[j] = False
if True in can:
    print(can.index(True))
else:
    print("impossible")


