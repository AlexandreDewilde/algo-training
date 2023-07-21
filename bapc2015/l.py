for _ in range(int(input())):
    l = list(map(int, input().split()))[:-1]

    ans = 0

    for i in range(1, len(l)):
        ans += max(0, l[i] - l[i - 1] * 2)
    print(ans)