n,m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

visited = [False]*n
order = []
def dfs(x, do=True):
    visited[x] = True
    if do:
        order.append(x)
    for adj in g[x]:
        if visited[adj]:
            continue
        dfs(adj, not do)
    if not do:
        order.append(x)


stack = []
order = []
visited = [False]*n
stack.append((0,True,False))
while stack:
    x,do,add = stack.pop()
    if add:
        order.append(x)
        continue
    if visited[x]:
        continue
    visited[x] = True
    if do:
        order.append(x)
    else:
        stack.append((x,False,True))

    for adj in g[x]:
        if visited[adj]:
            continue
        stack.append((adj, not do, False))

print(" ".join(str(el+1) for el in order))