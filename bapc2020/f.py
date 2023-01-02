import heapq
n, m, p,gg = map(int, input().split())

starts = []

for pp in (map(int, input().split())):
    starts.append(pp-1)
    
g = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, input().split())
    
    a -= 1
    b -= 1
    g[a].append((b,c))
    g[b].append((a,c))


pq = [(0,0)]
dst = [float("inf")]*n
dst[0] = 0
while pq:

    d, x = heapq.heappop(pq)
    if d > dst[x]:
        continue
    for adj, c in g[x]:
        if dst[adj] > dst[x] + c:
            dst[adj] = dst[x] + c
            heapq.heappush(pq, (dst[adj], adj))

ans = 0
for el in starts:
    ans += dst[el]
total = ans
cnt = [[0]*p for _ in range(n)]

for i, u in enumerate(starts):
    cnt[u][i] += 1

