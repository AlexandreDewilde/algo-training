for _ in range(int(input())):
    n = int(input())

    mx = (0,0)

    for i in range(n):
        a, b = map(int, input().split())
        
        if a <= 10:
            mx = max(mx, (b, i))
    print(mx[1]+1)