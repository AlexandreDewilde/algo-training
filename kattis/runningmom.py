import sys
sys.setrecursionlimit(int(1e6))
stdin = open(0)
n = int(stdin.readline())

g = {}
in_degree = {}
for _ in range(n):
    a1, a2 = stdin.readline().split()
    if a1 not in in_degree:
        in_degree[a1] = 0
    if a2 not in in_degree:
        in_degree[a2] = 0
    in_degree[a1] += 1
    if a1 not in g:
        g[a1] = [a2]
    else:
        g[a1].append(a2)

def dfs(x, vis):
    vis[x] = 1
    for adj in g.get(x, []):
        if adj not in vis:
            if dfs(adj, vis):
                return True
        elif vis[adj] == 1:
            return True
    vis[x] = 2
    return False
x = stdin.readline()
while x:
    vis = {}
    print(x[:-1], "safe" if dfs(x[:-1], vis) else "trapped")
    x = stdin.readline()