n = int(input())

grid = {}
for _ in range(n):
    x, y, r = map(int, input().split())
    
    x *= 10
    y *= 10
    r *= 10
    for i in range(x - r, x + r):
        for j in range(y - r, y + r):
            if (i - x) ** 2 + (j - y) ** 2<= r ** 2:
                grid[(i,j)] = 1

print(sum(grid.values()) / 10 ** 2)
