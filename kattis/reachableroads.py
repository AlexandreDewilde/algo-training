n = int(input())


for i in range(n):
    m = int(input())
    r = int(input())

    g = [[] for _ in range(m)]
    for _ in range(r):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    
    vis = [False]*m
    def dfs(x):
        vis[x] = True
        for adj in g[x]:
            if not vis[adj]:
                dfs(adj)
        
    ans = -1
    for i in range(m):
        if not vis[i]:
            dfs(i)
            ans += 1
    print(ans)