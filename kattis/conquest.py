import heapq

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

sizes = [int(input()) for _ in range(n)]

pq = [(0, 0)]
vis = [False] * n
vis[0] = True
current = sizes[0]

while pq:
    size, x = heapq.heappop(pq)
    if size >= current:
        continue
    current += size
    for adj in g[x]:
        if not vis[adj]:
            heapq.heappush(pq, (sizes[adj], adj))
            vis[adj] = True
print(current)