for _ in range(int(input())):
    l, r = map(int, input().split())
    
    start = (l + r) * (l + r + 1) // 2 + 1
    print(start + r)