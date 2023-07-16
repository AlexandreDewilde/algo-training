import heapq

v, e, c, k, m = map(int, input().split())

g = [[] for _ in range(v)]
for _ in range(e):
    a, b, w = map(int, input().split())
    g[a - 1].append((b - 1, w))
    g[b - 1].append((a - 1, w))

f = list(map(int, input().split()))


pq = [(0, 0)]
dst = [float("inf")] * v
dst[0] = 0

while pq:
    d, x = heapq.heappop(pq)
    if dst[x] < d:
        continue

    for adj, w in g[x]:
        if dst[x] + w < dst[adj]:
            dst[adj] = dst[x] + w
            heapq.heappush(pq, (dst[adj], adj))

places = []
for el in f:
    places.append(dst[el - 1])
places.sort()

print(places[min(m, k) - 1] * 2 if min(m, k) - 1 < len(places) and places[min(m, k) - 1] != float("inf") else -1)