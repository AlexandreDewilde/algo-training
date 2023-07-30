import heapq

n, m =map(int, input().split())

g = [[] for _ in range(n)]
ine = [0] * n
for _ in range(m):
    s,t,c = map(int, input().split())
    g[s-1].append((t-1, c))
    ine[t-1] += 1

pq = []
dst = [-1] * n
for i in range(n):
    if ine[i] == 0:
        pq.append((0, i))
        dst[i] = 0


while pq:
    d, x = heapq.heappop(pq)
    for adj, w in g[x]:
        if dst[adj] < dst[x] + w:
            dst[adj] = dst[x] + w
            heapq.heappush(pq, (-dst[adj], adj))

print(max(dst))