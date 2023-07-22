from collections import deque
import heapq

n, m, k = map(int, input().split())


t = list(map(int, input().split()))

g = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    g[x - 1].append((y - 1))
    g[y - 1].append(x - 1)

pq = [(t[n - 1], n - 1)]
dst = [float("inf")] * n
dst[n - 1] = t[n - 1]

while pq:
    d, x = heapq.heappop(pq)
    if d > dst[x]:
        continue
    
    for adj in g[x]:
        if dst[adj] > dst[x] + t[adj]:
            dst[adj] = dst[x] + t[adj]
            heapq.heappush(pq, (dst[adj], adj))

if dst[0] == dst[n - 1] + t[0]:
    if n == 2 and k == 1:
        print("impossible")
    elif k >= 2:
        print("N" + (n-k) * "S" + (k-2) * "N" + "N")
    else:
        print("S"*(n-k - 1) + "N"*k + "S")
    exit()

q = deque([0])

ass = [float("inf")] * n
ass[0] = k
current = k - 1
vis = [False] * n
vis[0] = True
while q:
    x = q.popleft()
    for adj in g[x]:
        if dst[adj] + t[x] == dst[x] and not vis[adj]:
            q.append(adj)
            vis[adj] = True
            ass[adj] = current
            current -= 1
for i in range(len(ass)):
    el = ass[i]
    if el == float("inf"):
        ass[i] = current
        current -= 1
print("".join(["N" if el > 0 else "S" for el in ass]))