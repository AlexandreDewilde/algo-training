h,w = map(int, input().split())

grid = []
l = []
for i in range(h):
    grid.append(list(map(int, input().split())))
    for j in range(w):
        l.append((grid[i][j], i,j))

l.sort(reverse=True)
vis = [[False]*w for _ in range(h)]

ans = 0
for val,i,j in l:
    if val <=1:
        break
    if vis[i][j]:
        continue
    ans += 1
    s = [(i,j)]
    while s:
        x,y = s.pop()
        vis[x][y] = True
        for xx,yy in [(x+1,y), (x-1, y), (x,y-1),(x,y+1)]:
            if 0<=xx<h and 0<=yy<w and not vis[xx][yy] and grid[x][y] >= grid[xx][yy]:
                s.append((xx,yy))

print(ans)
            