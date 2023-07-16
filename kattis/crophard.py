from itertools import permutations

perms = list(permutations([0,1,2]))


def calc(x):
    current = 1
    for el in x:
        current *= el
    return current

for case in range(int(input())):
    n, A, B, C, D, x, y, M = map(int, input().split())
    
    pts = [[0 for _ in range(3)] for _ in range(3)]
    pts[x%3][y%3] += 1
    for i in range(1, n):
        x = (A * x + B) % M
        y = (C * y + D) % M
        pts[x%3][y%3] += 1

    ans = 0
    for i in range(3):
        for j in range(3):
            if pts[i][j] < 3:
                continue
            ans += pts[i][j] * (pts[i][j] - 1) * (pts[i][j] - 2) // 6
        ans += calc(pts[i])
    for j in range(3):
        ans += calc([pts[k][j] for k in range(3)])
    for p in perms:
        ans += calc([pts[i][j] for i, j in zip(range(3), p)])

    print(f"Case #{case + 1}: {ans}")