m,n, q = map(int, input().split())


grid = [list(map(int, input().split())) for _ in range(m)]

parents = [i for i in range(m*n)]
rank = [0] * (n * m)

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    
    if pa == pb:
        return
    if rank[pa] > rank[pb]:
        parents[pb] = pa
    elif rank[pa] < rank[pb]:
        parents[pa] = pb
    else:
        rank[pa] += 1
        parents[pb] = pa
    


for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    