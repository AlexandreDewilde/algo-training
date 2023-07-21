for _ in range(int(input())):
    n, w = map(int, input().split())
    
    l = [0] * n
    r = [0] * n
    for i in range(n):
        l[i], r[i] = map(int, input().split())
    
    x = 0
    direction = [1] * n
    pos = [0] * n
    for i in range(n):
        pos[i] = l[i]
    for it in range(2 * w * w):
        fwd = [False] * (2 * w + 1)
        for i in range(n):
            if direction[i] == 1:
                fwd[pos[i]] = True
            pos[i] += direction[i]
            if pos[i] == l[i] or pos[i] == r[i]:
                direction[i] *= -1
        
        if fwd[x]:
            x += 1
        elif not fwd[x - 1]:
            x -= 1
        
        if x == w:
            print(it + 1)
            break
    else:
        print("IMPOSSIBLE")