from collections import defaultdict

p,v = map(int, input().split())

ped = []
for _ in range(p):
    a,b = map(int , input().split())
    ped.append((min(a,b),max(a,b)))

c = list(map(int, input().split()))

if v > p:
    print("impossible")
    exit()

occ = defaultdict(lambda: set())

for i,el in enumerate(c):
    occ[el].add(i)

still = []
ans = [0]*v
for i, (a,b) in sorted(enumerate(ped),key=lambda x: x[1]):
    if a == b and occ[a]:
        x = occ[a].pop()
        ans[x] = i
    elif a != b:
        still.append((a,b,i))

for a,b,i in still:
    a, b = min(a,b), max(a,b)
    if occ[a]:
        x = occ[a].pop()
        ans[x] = i
    elif occ[b]:
        x = occ[b].pop()
        ans[x] = i

for k in occ:
    if len(occ[k]):
        print("impossible")
        break
else:
    print(*(a+1 for a in ans), sep="\n")