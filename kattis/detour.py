import heapq
from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for _ in range(m):
    u, v, d = map(int, input().split())
    g[u].append((v, d))
    g[v].append((u, d))

pq = [(0, 1)]
dst = [float("inf")] * n
dst[1] = 0

while pq:
    d, x = heapq.heappop(pq)
    if d > dst[x]:
        continue
    for adj, w in g[x]:
        if dst[adj] > dst[x] + w:
            dst[adj] = dst[x] + w
            heapq.heappush(pq, (dst[adj], adj))

vis = [False] * n
q = deque([0])
vis[0] = True
par = [i for i in range(n)]
while q:
    x = q.popleft()
    for adj, w in g[x]:
        if not vis[adj] and dst[adj] + w != dst[x]:
            vis[adj] = True
            q.append(adj)
            par[adj] = x

if not vis[1]:
    print("impossible")
else:
    path = []
    l = 0
    current = 1

    while current != par[current]:
        path.append(current)
        current = par[current]
    path.append(0)
    print(len(path), " ".join(map(str, path[::-1])))
