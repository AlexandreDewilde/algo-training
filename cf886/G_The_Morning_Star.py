def sign(x):
    return 1 if x >= 0 else -1

for _ in range(int(input())):
    n = int(input())

    diff = {}
    d2 = {}
    X = {}
    Y = {}

    for _ in range(n):
        x,y = map(int, input().split())
        d2[y+x] = d2.get(x + y, 0) + 1
        diff[(y - x)] = diff.get(y - x, 0) + 1
        X[x] = X.get(x, 0) + 1
        Y[y] = Y.get(y, 0) + 1
    
    ans = 0

    for v in X.values():
        ans += v * (v - 1)
    for v in Y.values():
        ans += v * (v - 1)
    
    for v in diff.values():
        ans += v * (v - 1)
    
    for v in d2.values():
        ans += v * (v - 1)
    print(ans)