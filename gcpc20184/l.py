h, w = map(int, input().split())

grid = []
for _ in range(h+2):
    line = list(map(int, input().split()))
    grid.append(line)

ans = [["."]*w for _ in range(h)]
for i in range(1, h+1):
    for j in range(1, w+1):
        if grid[i-1][j-1] >= 1:
            ans[i-1][j-1] = "X"
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    grid[i+dx][j+dy] -= 1

for i in range(h+2):
    for j in range(w+2):
        
        if grid[i][j] != 0:
            print("impossible")
            exit()

for i in range(h):
    print("".join(ans[i]))
