import math

n = int(input())
t = list(map(int, input().split()))

s = list((map(int, input().split())))

comp = 0
used = 0
for ss, tt in sorted(zip(s, t)):
    if ss == -1:
        continue
    comp = max(comp, math.ceil((used + tt)/ss))
    used += tt
print(comp)

