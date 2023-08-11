for _ in range(int(input())):
    m = int(input())

    g = [[] for _ in range(m)]
    journey = []
    for i in range(m):
        h, a,b,c,d = input().split()
        a,b,c,d = map(int, [a,b,c,d])
        hr, minutes = map(int, h.split(":"))
        minutes += hr * 60
        end = minutes + abs(a - c) + abs(b - d)
        journey.append((minutes, end,a,b,c,d))
    
    for i in range(m):
        _, end, _, _,c, d = journey[i]
        for j in range(i+1, m):
            start, _, a, b, _, _ = journey[j]
            if end + abs(a - c) + abs(b - d) < start:
                g[i].append(j)
    
    vis = [False] * m
    match = [-1] * m
    def augment(u):
        if vis[u]:
            return False
        vis[u] = True
        for v in g[u]:
            if match[v] == -1 or augment(match[v]):
                match[v] = u
                return True
        return False

    ans = 0
    for i in range(m):
        for j in range(m):
            vis[j] = False
        
        if augment(i):
            ans += 1
    
    print(m - ans)