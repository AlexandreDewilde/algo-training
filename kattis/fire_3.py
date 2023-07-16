from collections import deque

r, c = map(int, input().split())

grid = [list(input()) for _ in range(r)]

pos = ("J", 0,0)
fires = []
for i in range(r):
    for j in range(c):
        if grid[i][j] == "J":
            pos = ("J", i, j)
        if grid[i][j] == "F":
            fires.append(("F", i, j))

q = deque([*fires, pos])
dst = [[float("inf")] * c for _ in range(r)]
dst[pos[1]][pos[2]] = 0

ans = float("inf")
while q:
    t, x, y = q.popleft()
    if t == "J" and (x == 0 or x == r - 1 or y == 0 or y == c -1):
        ans = dst[x][y] + 1
        break
    for dx, dy in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        if not (0 <= dx < r and 0 <= dy < c):
            continue
        if t == "F" and grid[dx][dy] in {".", "J"}:
            grid[dx][dy] = "F"
            q.append(("F", dx, dy))
        elif t == "J" and grid[dx][dy] == "." and dst[dx][dy] == float("inf"):
            dst[dx][dy] = dst[x][y] + 1
            grid[dx][dy] = "J"
            q.append(("J", dx, dy))

print(ans if float("inf") != ans else "IMPOSSIBLE")