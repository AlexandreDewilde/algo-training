n, m = map(int, input().split())

g = [[] for _ in range(n)]
g_inv = [[] for _ in range(n)]
ine = [0] * n
out = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g_inv[v-1].append(u-1)
    ine[v-1] += 1
    out[u-1] += 1

done = [0] * n
length = [0] * n


current = [i for i in range(n) if out[i] == 0]

stack = current

while stack:
    x = stack.pop()
    done[x] += 1
    if done[x] < out[x]:
        continue

    for adj in g_inv[x]:
        stack.append(adj)
        length[adj] = max(length[adj], length[x] + 1)

mx = max(length)

ans = mx


stack = [(i,0) for i in range(n) if length[i] == mx]

vis = [False] * n
depths = [[0,0] for _ in range(mx+1)]

while stack:
    x, depth = stack.pop()
    # depths[depth][0] += 1
    if vis[x]:
        continue
    vis[x] = True
    for adj in g[x]:
        if depths[depth][0] < length[adj] + 1:
            depths[depth][1] = depths[depth][0]
            depths[depth][0] = length[adj] + 1
        elif depths[depth][1] < length[adj] + 1:
            depths[depth][1] = length[adj] + 1
        if length[adj] != length[x] - 1:
            continue
        # depths[depth][1] += 1
        stack.append((adj, depth+1))

for i, (_, x) in enumerate(depths):
    ans = min(x + i, ans)
print(ans)

