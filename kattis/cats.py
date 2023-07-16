for _ in range(int(input())):
    m, c = map(int, input().split())
    
    edges = []

    for _ in range(c * (c - 1) // 2):
        edges.append((tuple(map(int, input().split()))))
        
    
    edges.sort(key=lambda x: x[2])

    parents = [i for i in range(c)]
    rank = [0] * c

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
            elif rank[a] < rank[b]:
                parents[a] = b
            else:
                parents[b] = a
                rank[a] += 1
    ans = 0

    for a, b, w in edges:
        if find(a) != find(b):
            union(a, b)
            ans += w
    print("yes" if ans + c <= m else "no")