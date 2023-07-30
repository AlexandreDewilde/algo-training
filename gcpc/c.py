from collections import deque
import sys
from math import gcd

n, m, k = map(int, sys.stdin.readline().split())

h = list(map(int, sys.stdin.readline().split()))

g = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    
    g[a-1].append(b-1)
    g[b-1].append(a-1)

def bfs(x):
    q = deque([x])
    dst = [float("inf")]*n
    dst[x] = 0
    while q:
        x = q.popleft()
        for adj in g[x]:
            if dst[adj] == float("inf"):
                dst[adj] = dst[x] + 1
                q.append(adj)

    return dst

dst0 = bfs(0)
dstn = bfs(n - 1)
s = sum(dstn[x - 1] for x in h)

ans = dst0[n - 1] * (k - 1)
res = min(dst0[i - 1] * (k - 1) + s - dstn[i - 1]  for i in h)
ans = min(ans, res)
g = gcd(ans, k - 1)

print(f"{ans //g}/{(k-1) // g}")
 