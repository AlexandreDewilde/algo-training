n = int(input())


grid_size = 100

grid = [[[[] for _ in range(grid_size)] for _ in range(grid_size)] for _ in range(grid_size)]
coords_to_grid = int(1e9) // grid_size
planets = []

for _ in range(n):

    x,y,z = map(int, input().split())
    planets.append((x,y,z))
    grid[x//coords_to_grid][y//coords_to_grid][z//coords_to_grid].append((x,y,z))


def dst(p1, p2):
    total = 0
    for i in range(3):
        total += (p1[i]-p2[i])**2
    return total ** 0.5

ans = float("inf")
for x,y,z in planets:
    for dx in range(-1,2):
        for dy in range(-1,2):
            for dz in range(-1,2):
                xx = dx + x//coords_to_grid
                yy = dy + y//coords_to_grid
                zz = dz + z//coords_to_grid
                if 0 <= xx < len(grid) and 0 <= yy < len(grid) and 0<=zz < len(grid):
                    for planet in grid[xx][yy][zz]:
                        if planet == (x,y,z):
                            continue
                        ans = min(ans, dst((x,y,z), planet))
    
print(ans)

