import sys
sys.setrecursionlimit(int(1e6))

n, q = map(int, input().split())


parents = [i for i in range(n)]

rank = [0] * n
size = [1] * n

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        if rank[a] > rank[b]:
            parents[b] = a
            size[a] += size[b]
        elif rank[a] < rank[b]:
            parents[a] = b
            size[b] += size[a]
        else:
            parents[a] = b
            rank[b] += 1
            size[b] += size[a]

for _ in range(q):
    s = input()
    if s[0] == "t":
        a, b = map(int, s.split()[1:])
        union(a - 1, b - 1)
    else:
        a = int(s.split()[1])
        print(size[find(a - 1)])