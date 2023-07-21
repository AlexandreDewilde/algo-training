for _ in range(int(input())):
    n, m = map(int, input().split())
    
    g = [[] for _ in range(n)]
    constrainst = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        
        constrainst.append((a - 1,b - 1,d))
        g[a - 1].append((b - 1, d))
        g[b - 1].append((a - 1, -d))
    
    vis = [False] * n
    pos = [0]*n

    def dfs(i):
        vis[i] = True
        stack = [i]
        while stack:
            i = stack.pop()
            for adj, w in g[i]:
                if not vis[adj]:
                    pos[adj] = pos[i] + w
                    vis[adj] = True
                    stack.append(adj)

    for i in range(n):
        if not vis[i]:
            dfs(i)
    
    for a, b, d in constrainst:
        if pos[a] + d != pos[b]:
            print("NO")
            break
    else:
        print("YES")
                