import sys
sys.setrecursionlimit(int(1e6))
n,h = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

leaves = []
def dfs(x, par):
    found = False
    for adj in g[x]:
        if adj == par:
            continue
        dfs(adj, x)
        found = True
    if not found:
        leaves.append(x)

start = 0
for i in range(n):
    if len(g[i]) > 2:
        start = i
dfs(start,-1)
mid = len(leaves)//2
print(mid + len(leaves) % 2)
for i in range(mid):
    print(leaves[i], leaves[i+mid])

if len(leaves) & 1:
    print(leaves[-1], 0)
