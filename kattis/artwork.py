n, m, q = map(int, input().split())

grid = [[0]*n for _ in range(m)]

req = []

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    req.append((x1, y1, x2, y2))
    
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            grid[i][x1] += 1
    
    else:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][i] += 1

parents = [[(i,j) for j in range(n)] for i in range(m)]
rank = [[0] * n for _ in range(m)]
regions = n * m
colored = n * m
def find(x, y):
    if parents[x][y] != (x,y):
        parents[x][y] = find(*parents[x][y])
    return parents[x][y]

def union(a, b):
    global regions
    a = find(*a)
    b = find(*b)

    if a != b:
        regions -= 1
        if rank[a[0]][a[1]] > rank[b[0]][b[1]]:
            parents[b[0]][b[1]] = a
        
        elif rank[a[0]][a[1]] < rank[b[0]][b[1]]:
            parents[a[0]][a[1]] = b
        
        else:
            parents[b[0]][b[1]] = a
            rank[a[0]][a[1]] += 1
def merge(i,j):
    if grid[i][j] != 0:
        return
    global colored
    colored -= 1
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
            union((i, j), (x, y))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        merge(i,j)

ans = [regions - colored]

for x1, y1, x2, y2 in req[::-1]:
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            grid[i][x1] -= 1
            merge(i, x1)
    
    else:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][i] -= 1
            merge(y1, i)
    # print(regions, colored)
    ans.append(regions - colored)

print("\n".join(map(str, ans[::-1][1:])))