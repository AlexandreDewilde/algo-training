n, m = map(int, input().split())


grid = [list(input()) for _ in range(n)]

vis = [[-1] * m for _ in range(n)]

def dfs(x, y, id_):
    stack = [(x,y)]
    vis[x][y] = id_
    while stack:
        x, y, = stack.pop()
        for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= xx < n and 0 <= yy < m and vis[xx][yy] == -1 and grid[xx][yy] == grid[x][y]:
                vis[xx][yy] = id_
                stack.append((xx,yy))

nb_comps = 0
for i in range(n):
    for j in range(m):
        if vis[i][j] == -1:
            dfs(i, j, nb_comps)
            nb_comps += 1
g = [[] for _ in range(nb_comps)]

done = [[False]*m for _ in range(m)]
def dfs(a, b):
    stack = [(a,b)]
    done[a][b] = True
    added = set([vis[a][b]])
    while stack:
        x, y = stack.pop()
        for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= xx < n and 0 <= yy < m and done[xx][yy] == False and grid[xx][yy] == grid[x][y]:
                done[xx][yy] = True
                stack.append((xx,yy))
            elif 0 <= xx < n and 0 <= yy < m and vis[xx][yy] not in added:
                g[vis[a][b]].append(vis[xx][yy])
                added.add(vis[xx][yy])

for i in range(n):
    for j in range(m):
        if not done[i][j]:
            dfs(i, j)
match = [-1] * nb_comps
vis = [False] * nb_comps

def augment(x):
    if vis[x]:
        return False
    vis[x] = True
    for adj in g[x]:
        if match[adj] == -1 or augment(match[adj]):
            match[adj] = x
            return True

    return False

ans = 0
for i in range(nb_comps):
    for j in range(nb_comps): vis[j] = False
    if augment(i): ans += 1

print(ans, g, nb_comps, match)
