n, m, q = map(int, input().split())

g = [set() for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].add(v)
    g[v].add(u)

reqs = []

for i in range(q):
    t, u, v = map(int, input().split())
    reqs.append((t, u, v))
    if t == 0:
        g[u].remove(v)
        g[v].remove(u)

parents = [i for i in range(n)]
ranks = [0]*n

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return

    if ranks[a] < ranks[b]:
        a, b = b, a

    parents[b] = a
    ranks[a] += ranks[b]


def dfs(x, vis):
    stack = [x]
    vis[x] = True
    while stack:
        x = stack.pop()
        for adj in g[x]:
            if not vis[adj]:
                stack.append(adj)
                union(x, adj)
                vis[adj] = True

vis = [False] * n

for i in range(n):
    if not vis[i]:
        dfs(i, vis)

ans = []
for req in reqs[::-1]:
    t, u, v = req

    if t == 0:
        union(u, v)
    else:
        ans.append("safe" if find(u) == find(v) else "unsafe")

print("\n".join(ans[::-1]))