from collections import deque
import sys

w, h = map(int, input().split())

grid = [sys.stdin.readline() for _ in range(h)]
start = (-1,-1)
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            start =(i,j)
            break

s = list(sys.stdin.readline().replace("\n", ""))
delta = {"E": (0, 1), "W": (0,-1), "N":(-1, 0), "S":(1,0)}

q = deque([start])
dst = [[[float("inf")]*2 for _ in range(w)] for _ in range(h)]
dst[start[0]][start[1]][0] = dst[start[0]][start[1]][1] = 0

while q:
    x,y = q.popleft()
    if dst[x][y][0] == len(s):
        break

    for dir, (dx, dy) in delta.items():
        xx = x + dx
        yy = y + dy
        if not (0<= xx < h and 0 <= yy < w) or dst[xx][yy][0] < dst[x][y][0] + 1 or dst[xx][yy][1] != float("inf") or grid[xx][yy] != ".":
            continue
        if dst[xx][yy][0] == float("inf"):
            q.append((xx, yy))
        dst[xx][yy][0] = dst[x][y][0] + 1
        if not dir == s[dst[x][y][0]]:
            dst[xx][yy][1] = dst[x][y][1] + 1
        


ans = []
for i in range(h):
    for j in range(w):
        if dst[i][j][1] == len(s):
            ans.append("!")
        else:
            ans.append(grid[i][j])
    ans.append("\n")

print("".join(ans))
