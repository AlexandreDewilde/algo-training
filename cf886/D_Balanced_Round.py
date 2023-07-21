for _ in range(int(input())):
    n, k = map(int, input().split())
    
    a = sorted(list(map(int, input().split())))

    current = 1
    ans = 1
    for i in range(1, n):
        if abs(a[i] - a[i - 1]) <= k:
            current += 1
            ans = max(ans, current)
        else:
            current = 1
    print(n - ans)