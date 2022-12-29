from collections import deque


h,w = map(int, input().split())

grid = []

for _ in range(h):
    grid.append(list(map(int, input().split())))

def lowest(x,y,n):
    l = (float("inf"), float("inf"))
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        xx = x + dx
        yy = y + dy
        if 0<=xx < h and 0<= yy < w:
            l = min(l, (abs(n-grid[xx][yy]), abs(grid[x][y]-grid[xx][yy]) ))
    return l

def bfs(x,y):
    q = deque([(x,y)])

    dst = [[float("inf")]*w for _ in range(h)]
    dst[x][y] = 0

    while q:
        i,j = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            ii = i + dx
            jj = j + dy
            if 0<= ii < h and 0<= jj < w and dst[ii][jj] == float("inf"):
                diff_dest, diff_adj = lowest(ii,jj,grid[x][y])
                if diff_dest == abs(grid[x][y]-grid[i][j]) and diff_adj == abs(grid[i][j]-grid[ii][jj]):
        
                    dst[ii][jj] = dst[i][j] + 1
                    q.append((ii,jj))
    return dst

dsts = [[bfs(i,j) for j in range(w)] for i in range(h)]

ans = (float("inf"), 0, 0)
for i in range(h):
    for j in range(w):
        current = 0
        for ii in range(h):
            for jj in range(w):
                current = max(current, dsts[ii][jj][i][j])
        ans = min(ans, (current, i,j))
if ans[0] == float("inf"):
    print("impossible")
else:
    print(grid[ans[1]][ans[2]], ans[0])