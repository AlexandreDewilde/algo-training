from collections import deque

R,C = map(int, input().split())

grid = []
for i in range(R):
    grid.append(list(input()))

r,c = map(int, input().split())
r-=1
c-=1

q = deque([(r,c)])
dst = [[float("inf")]*C for _ in range(R)]
dst[r][c] = 1
while q:
    x,y = q.popleft()
    if x == 0 or y==0 or x == R-1 or y == C-1:
        print(dst[x][y])
        break
    for xx,yy in [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]:
        if 0 <= xx < R and 0 <= yy < C and dst[xx][yy] == float("inf") and grid[xx][yy] != "#":
            if grid[xx][yy] == "D":
                q.appendleft((xx,yy))
                dst[xx][yy] = dst[x][y]
            else:
                q.append((xx,yy))
                dst[xx][yy] = dst[x][y] +1
