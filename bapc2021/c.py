#base on jury slides
#based on ragnar solution 

n, m = map(int, input().split())

grid = []

for i in range(n//2):
    idx = set()
    for j,char in enumerate(input()):
        if char == "#":
            idx.add(j)
    line = []
    nb = 0
    for j,char in enumerate(input()):
        if j in idx or char == "#":
            nb |= 1<<j

    grid.append(nb)

grid = grid[::-1]

#based on ragnar solution
poss = []
for i in range(1<<(m-1)):
    done = True
    tot = 0
    for j in range(m-1):
        if i & (1<<j):
            tot += 1
        if (i&(1<<j)) and (i&(1<<(j+1))):
            done = False
            break
    if done:
        poss.append((i, tot))

dp = [0]*len(poss)
def can(s1, s2):
    return s2 == (s2 & ((s1 << 1) | s1 | (s1>>1)))

def cover(grid_line, cov):
    return grid_line == (grid_line & (cov | (cov<<1)))
            

for h in range(n//2):
    new_dp = [float("inf")]*len(poss)
    for i, (p1,c1) in enumerate(poss):
        if dp[i] == float("inf"):
            continue
        for j, (p2,c2) in enumerate(poss):
            if can(p1, p2) and cover(grid[h], p2):
                new_dp[j] = min(new_dp[j], dp[i] + c2)
    dp = new_dp
print(min(dp))
