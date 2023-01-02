import heapq


n, m = map(int, input().split())

g = [[] for _ in range(n)]
pq = []
dst = [float("inf")]*n
for i in range(m):
    c, a = map(int, input().split())
    dst[c-1] = a
    heapq.heappush(pq, (a,c-1))
    
b = list(map(int, input().split()))
for i in range(n-1):
    g[i].append((i+1, b[i]))
    g[i+1].append((i, b[i]))
g[n-1].append((0, b[n-1]))
g[0].append((n-1, b[n-1]))

vis = [False]*n
ans = 0
while pq:
    cost,x = heapq.heappop(pq)
    if cost > dst[x]:
        continue
    ans += cost
    vis[x] = True
    for adj,c in g[x]:
        if not vis[adj] and dst[adj] > c:
            heapq.heappush(pq, (c, adj))
            dst[adj] = c
print(ans)

