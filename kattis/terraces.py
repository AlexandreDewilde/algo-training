
x, y = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(y)]

coords = []

for i in range(y):
    for j in range(x):
        coords.append((grid[i][j], i, j))

coords.sort()

vis = [[False]*x for _ in range(y)]
def dfs(x, y, base):
    stack = [(x,y)]
    vis[x][y] = True
    ret = 0
    while stack:
        x, y = stack.pop()
        for xx, yy in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if 0<= xx < len(grid) and 0 <= yy < len(grid[0]) and not vis[xx][yy] and grid[xx][yy] >= grid[x][y]:
                ret += grid[xx][yy] == base
                vis[xx][yy] = True
                stack.append((xx,yy))
    return ret

ans = 0
for _, x, y in coords:
    if not vis[x][y]:
        ans += dfs(x,y, _) + 1

print(ans)