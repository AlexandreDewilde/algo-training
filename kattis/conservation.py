from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    stage = [0] + list(map(int, input().split()))

    g = [[] for _ in range(n + 1)]
    ine = [0] * (n + 1)

    for _ in range(m):
        x, y = map(int, input().split())
        ine[y] += 1        
        g[x].append(y)

    for i in range(1, n + 1):
        if ine[i] == 0:
            g[0].append(i)
            ine[i] += 1

    vis = [False] * (n + 1)
    current_ine = [0] * (n + 1)
    def bfs(x):
        ans = 0
        q = deque([x])
        current = stage[x]
        while q:
            if current == 1:
                x = q.popleft()
            else:
                x = q.pop()
            
            if current != stage[x]:
                ans += 1
                current = stage[x]
  
            for adj in g[x]:
                current_ine[adj] += 1
                if current_ine[adj] == ine[adj]:
                    if stage[adj] == 1:
                        q.appendleft(adj)
                    else:
                        q.append(adj)
        return ans

    stage[0] = 1
    ans = bfs(0)
    for i in range(n + 1):
        current_ine[i] = 0
        vis[i] = False
    stage[0] = 2
    a2 = bfs(0)
    print(min(ans, a2))

