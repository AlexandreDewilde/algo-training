for _ in range(int(input())):
    n = int(input())
    p = [int(input()) for _ in range(n)]

    smallest = p[n - 1]
    ans = []
    for i in range(n - 2, -1, -1):
        smallest = min(smallest, p[i])
        if smallest < p[i]:
            ans.append(p[i])
    print(len(ans))
    if ans:
        ans.sort()
        print("\n".join(map(str, ans)))