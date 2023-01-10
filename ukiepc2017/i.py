import sys
input = sys.stdin.readline
n = int(input())

h = list(map(int, input().split()))

t = int(input())

best = h[0]
for el in h:
    if (t%best) > t%el:
        best = el

print(best)
