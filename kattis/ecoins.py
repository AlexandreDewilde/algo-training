for _ in range(int(input())):
    if _: input()
    m, s = map(int, input().split())
    
    l = []
    for _ in range(m):
        x, y = map(int, input().split())
        l.append((x,y))
    dp = [[float("inf")]*301 for _ in range(301)]

    dp[0][0] = 0
    for x, y in l:
        for i in range(x, len(dp)):
            for j in range(y, len(dp)):
                dp[i][j] = min(dp[i][j], 1 + dp[i - x][j - y])
    
    ans = float("inf")
    for i in range(s+1):
        target = (s ** 2 - i ** 2) ** 0.5
        if abs(target - round(target)) > 1e-9 or round(target) < 0:
            continue
        # print(target)
        ans = min(ans, dp[i][round(target)])


    print(ans if ans != float("inf") else "not possible")