import heapq
from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    a,b, d = map(int, input().split())
    g[a].append((b,d))
    g[b].append((a,d))

pq = [(0,1)]
par = [-1]*n
dst = [float("inf")]*n
dst[1] = 0

while pq:
    d,x = heapq.heappop(pq)
    if d > dst[x]:
        continue
    for adj,w in g[x]:
        if d + w < dst[adj]:
            dst[adj] = d + w
            heapq.heappush(pq, (dst[adj], adj))
            par[adj] = x

par = [-1]*n
par[0] = 0
vis = [False]*n
q = deque([0])

while q:
    x = q.pop()
    vis[x] = True
    for adj,w in g[x]:
        if not vis[adj] and dst[x] != dst[adj] + w:
            q.append(adj)
            par[adj] = x

if not vis[1] or par[1] == -1:
    print("impossible")
else:
    current = 1
    path = []
    while current != 0:
        path.append(current)
        current = par[current]
    path.append(0)
    print(len(path), *path[::-1])