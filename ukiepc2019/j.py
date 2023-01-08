import sys
import math
import heapq

input = sys.stdin.readline

n = int(input())

t = list(map(int, input().split()))

m = int(input())

q = list(map(int, input().split()))

g = [[] for _ in range(m)]

angle = 360 / m

for j in range(m):
    for i in range(m):
        w = abs(2*math.sin(math.radians(angle/2*i)))
        g[j].append(((j+i)%m, w))

pq = [(1, 1, i) for i in range(m) if q[i] == t[0]]
dst = [[float("inf")]*(n+1) for _ in range(m)]


while pq:
    d, step, x = heapq.heappop(pq)
    if d > dst[x][step-1]:
        continue
    if step == n:
        print(d)
        break
    for adj, w in g[x]:
        if q[adj] == t[step] and dst[adj][step] > d + w:
            dst[adj][step] = d + w
            heapq.heappush(pq, (dst[adj][step], step+1, adj))
