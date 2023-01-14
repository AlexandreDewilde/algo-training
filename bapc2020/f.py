n, m, p, G =map(int, input().split())

v = list(map(lambda x: int(x)-1, input().split()))

g = [[] for _ in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b,c))
    g[b].append((a,c))

import heapq

pq = [(0,0)]

dst = [float("inf")]* n
dst[0] = 0
while pq:
    d, x = heapq.heappop(pq)

    for adj, w in g[x]:
        if dst[adj] > d + w:
            dst[adj] = d + w
            heapq.heappush(pq, (dst[adj], adj))
            
ans = sum(dst[el] for el in v)
total = ans
peoples = sorted(v, key=lambda x: -dst[x])

stations = [set() for i in range(n)]

for i,people in enumerate(peoples):
    stations[people].add(i)

for sta in sorted(range(n), key=lambda x:-dst[x]):
    for adj, w in g[sta]:
        if dst[sta] == dst[adj] + w:
            stations[adj] |= stations[sta]
    ans = min(ans, total + len(stations[sta])*G - dst[sta]*len(stations[sta]))
print(ans)