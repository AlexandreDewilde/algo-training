for _ in range(int(input())):
    c, b = map(int, input().split())
    

    g = [0] * c
    for _ in range(b):
        i,j = map(int, input().split())
        g[i] |= (1<<j)
        g[j] |= (1<<i)
    
    def onecolor(mask):
        for i in range(c):
            if not ((1<<i) & mask):
                continue
            for j in range(i+1, c):
                if (g[i] & (1 << j)) & mask:
                    return False
        return True
    
    def twocolor(mask):
        vis = 0
        color = 0
        def dfs(i, current, vis, color):
            vis |= (1<<i)
            color |= (1<<i) & current
            for j in range(c):
                if (g[i] & (1<<j) & mask) and not (vis & (1<<j)):
                    if not dfs(j, ~current, vis, color):
                        return False
                elif (g[i] & (1<<j) & mask) and (vis & (1<<j)) and (color & (1<<i)) == (color & (1<<j)):
                    return False
            
            return True
        
        for i in range(c):
            if not ((1 << i) & vis) and (1<<i) & mask:
                if not dfs(i, 0, vis, color):
                    return False 

        return True
    
    def threecolor():
        for i in range(1, 1 << c):
            if onecolor(i) and twocolor(~i & 0b111111111111111111):
                return True
        return False
    
    def fourcolor():
        for i in range(1, 1<<c):
            if twocolor(i) and twocolor(~i):
                return True
        return False
    
    if onecolor(~0):
        print(1)
    
    elif twocolor(~0):
        print(2)
    
    elif threecolor():
        print(3)
    
    elif fourcolor():
        print(4)
        
    else:
        print("many")