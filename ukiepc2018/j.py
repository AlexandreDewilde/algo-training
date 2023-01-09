import sys
import math

input = sys.stdin.readline

n,m,f = input().split()

n = int(n)
m = int(m)
f = float(f)

if n == 1:
    print(m)
    exit()

def ff(d):
    return (m-(f*d)**2)/ (n-d)

l = 1
r = n - 1
while r - l >= 1:
    m1 = l + (r-l) / 3
    m2 = r - (r-l) / 3
    if ff(m1) < ff(m2):
        l = m1
    else:
        r = m2
    print(m1)

print(max(ff(int(l)), ff(math.ceil(l))))