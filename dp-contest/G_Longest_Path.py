n, m = map(int, input().split())
import sys
sys.setrecursionlimit(int(1e6))

g = [[] for _ in range(n)]
for _ in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)

dp = [0] * n
vis = [False] * n

def dfs(x):
    if vis[x]:
        return
    vis[x] = True
    for adj in g[x]:
        if not vis[adj]:
            dfs(adj)
    
        dp[x] = max(dp[x], 1 + dp[adj])

for i in range(n):
    if not vis[i]:
        dfs(i)

print(max(dp))
