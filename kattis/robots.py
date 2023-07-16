from collections import deque

for _ in range(int(input())):
    K, n = map(int, input().split())

    r = list(map(int, input().split()))
    g = list(map(int, input().split()))

    gr = [[] for _ in range(n)]
    gg = [[] for _ in range(n)]

    for i in range(n):
        gr[r[i]].append(i)
        gg[g[i]].append(i)
    

    vis = [[False] * n for _ in range(n)]

    queue = deque()
    for i in range(n):
        vis[i][i] = True
        queue.append((i,i))
    
    while queue:
        i,j = queue.popleft()

        for x in gr[i]:
            for y in gr[j]:
                if not vis[x][y]:
                    vis[x][y] = True
                    queue.append((x,y))
        
        for x in gg[i]:
            for y in gg[j]:
                if not vis[x][y]:
                    vis[x][y] = True
                    queue.append((x,y))
    
    good = True

    for i in range(n):
        for j in range(n):
            if not vis[i][j]:
                good = False
                break
        else:
            continue
        break
    print(K, "YES" if good else "NO")


