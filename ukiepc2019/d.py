import sys
n, k = map(int, sys.stdin.readline().split())

l = []
for i in range(n):
    x,y,z = map(float, sys.stdin.readline().split())
    l.append((x**2+y**2+z**2)**0.5)

l.sort()

print(l[k-1])