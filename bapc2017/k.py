n = int(input())

g = [[] for _ in range(n)]
for i in range(n):
    line = list(input())
    for j in range(n):
        if line[j] == "1":
            g[i].append(j)

vis = [False]*n
sol = []
def dfs(x):
    vis[x] = True
    for adj in g[x]:
        if not vis[adj]:
            dfs(adj)
    sol.append(x)

dfs(0)

if len(sol) == n:
    print(*sol)
else:
    print("impossible")