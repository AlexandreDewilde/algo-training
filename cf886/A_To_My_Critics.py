for _ in range(int(input())):
    l = sorted(list(map(int, input().split())))

    print("YES" if sum(l[1:]) >= 10 else "NO")
    
