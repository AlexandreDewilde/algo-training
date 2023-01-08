import sys
import math
input = sys.stdin.readline

n,h = map(int, input().split())

v = list(map(int, input().split()))

occ = {}

hands = [set()]
current = 0
for el in v:
    occ[el] = occ.get(el, 0) + 1

k = n // h
hands = [[] for _ in range(k)]

current = 0
for el, oc in occ.items():
    for i in range(current, min(k, current+oc)):
        hands[i].append(el)
        if len(hands[i]) >= h:
            current = i + 1

if k == 0 or len(hands[0]) < h:
    print("impossible")
    exit()

for i in range(len(hands)):
    if len(hands[i]) == h:
        print(*hands[i])

