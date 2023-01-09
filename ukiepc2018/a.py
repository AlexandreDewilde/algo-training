import sys
input = sys.stdin.readline

n, c = map(int, input().split())

w = list(map(int, input().split()))

g = [[] for _ in range(n)]

for i in range(c):
    a,b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

visited = [False]*n
def dfs(x, cp):
    cp[w[x]] = cp.get(w[x],0)+1
    visited[x] = True
    for adj in g[x]:
        if not visited[adj]:
            dfs(adj, cp)
ans = 0
for i in range(n):
    if visited[i]:
        continue
    comp = {}
    dfs(i, comp)
    mx = w[i]
    for k in comp:
        if comp[k] > comp[mx]:
            mx = k
    ans += sum(comp.values()) - comp[mx]
print(ans)