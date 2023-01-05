import math

n = int(input())
mappings = {}

l = []
for i in range(n):
    o,w,r = input().split()
    r = float(r)
    if o not in mappings:
        mappings[o] = len(mappings)
    if w not in mappings:
        mappings[w] = len(mappings)
    l.append((mappings[w], mappings[o], r))

if "pink" not in mappings:
    mappings["pink"] = len(mappings)

best = [float("-inf")]*len(mappings)
best[mappings["pink"]] = 0
for i in range(n):
    go, to, r = l[i]
    best[to] = max(best[to], best[go]+math.log(r))

if "blue" not in mappings:
    print(0)
else:
    if best[mappings["blue"]] > math.log(10):
        print(10)
    else:
        print(math.exp(best[mappings["blue"]]))
    