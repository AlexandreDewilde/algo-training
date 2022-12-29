n = int(input())



grid = [[[[] for _ in range(100)] for _ in range(100)] for _ in range(100)]

planets = []
for _ in range(n):

    x,y,z = map(int, input().split())
    planets.append((x,y,z))
    grid[x//10_000_000][y//10_000_000][z//10_000_000].append((x,y,z))


def dst(p1, p2):
    total = 0
    for i in range(3):
        total += (p1[i]-p2[i])**2
    return total ** 0.5

ans = float("inf")
for x,y,z in planets:
    delta = [(0,0,-1),(0,-1,0),(-1,0,0),(1,0,0),(0,1,0),(0,0,1)]

    for planet in grid[x//10_000_000][y//10_000_000][z//10_000_000]:
        if planet == (x,y,z):
            continue
        ans = min(ans, dst((x,y,z), planet))
    for dx,dy,dz in delta:
        xx = dx + x//10_000_000
        yy = dy + y//10_000_000
        zz = dz + z//10_000_000
        if 0 <= xx < len(grid) and 0 <= yy < len(grid) and 0<=zz < len(grid):
            for planet in grid[xx][yy][zz]:
                ans = min(ans, dst((x,y,z), planet))
    
print(ans)

