n, m = map(int, input().split())


grid = [list(input()) for _ in range(n)]

comps = [[-1] * m for _ in range(n)]

def dfs(x, y, id_):
    stack = [(x,y)]
    comps[x][y] = id_
    while stack:
        x, y, = stack.pop()
        for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= xx < n and 0 <= yy < m and comps[xx][yy] == -1 and grid[xx][yy] == grid[x][y]:
                comps[xx][yy] = id_
                stack.append((xx,yy))

nb_comps = 0
for i in range(n):
    for j in range(m):
        if comps[i][j] == -1:
            dfs(i, j, nb_comps)
            nb_comps += 1

is_border = [False] * nb_comps

for i in range(n):
    is_border[comps[i][-0]] |= True
    is_border[comps[i][-1]] |= True

for j in range(m):
    is_border[comps[-0][j]] |= True
    is_border[comps[-1][j]] |= True

ans = sum(is_border)

v1 = 0
v2 = 0
ids = [-1] * nb_comps
for i in range(n):
    for j in range(m):
        if ids[comps[i][j]] != -1 or is_border[comps[i][j]]:
            continue
        if grid[i][j] == "1":
            ids[comps[i][j]] = v1
            v1 += 1
        else:
            ids[comps[i][j]] = v2
            v2 += 1
        
g = [[] for _ in range(v1)]
added = set()
vis = [[False]*m for _ in range(n)]
def dfs2(x, y):
    vis[x][y] = True
    for xx, yy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= xx < n and 0 <= yy < m and vis[xx][yy] == False and grid[xx][yy] == grid[x][y] and not is_border[comps[xx][yy]]:
            dfs2(xx, yy)
        elif 0 <= xx < n and 0 <= yy < m and vis[xx][yy] == False and not is_border[comps[xx][yy]]:
            if grid[x][y] == "1" and (ids[comps[x][y]], ids[comps[xx][yy]]) not in added:
                added.add((ids[comps[x][y]], ids[comps[xx][yy]]))
                g[ids[comps[x][y]]].append(ids[comps[xx][yy]])
            elif grid[x][y] == "0" and (ids[comps[xx][yy]], ids[comps[x][y]]) not in added:
                added.add((ids[comps[xx][yy]], ids[comps[x][y]]))
                g[ids[comps[xx][yy]]].append(ids[comps[x][y]])
for i in range(n):
    for j in range(m):
        if not vis[i][j] and not is_border[comps[i][j]]:
            dfs2(i, j)

match = [-1] * v2
vis = [False] * v1

def augment(v):
    if vis[v]:
        return False
    vis[v] = True
    for u in g[v]:
        if match[u] == -1 or augment(match[u]):
            match[u] = v
            return True
        
    return False

for i in range(v1):
    for j in range(v1):
        vis[j] = False
    if augment(i):
        ans += 1
print(ans)