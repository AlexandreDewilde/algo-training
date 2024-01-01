n, d, c = map(int, input().split())

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))

common = len(set(p1).intersection(p2))
p1 = c - common
p2 = c - common


combs = [[0]*(n+1) for _ in range(n+1)]
combs[0][0] = combs[1][1] = combs[1][0] = 1
for i in range(2, n+1):
    combs[i][0] = combs[i][i] = 1
    for j in range(i):
        combs[i][j] = combs[i-1][j] + combs[i-1][j-1]

import sys
sys.setrecursionlimit(int(1e6))
mem = {}
def dp(cp1, cp2, cCommon, it=1):
    if it < 1e-9:
        return 0
    if (cp1, cp2, cCommon) in mem:
        return mem[(cp1, cp2, cCommon)]

    if cCommon == 0 and (cp1 == 0 or cp2 == 0):
        # print(cCommon, cp1, cp2)
        return 0
    total = 1
    for i in range(min(cCommon, d)+1):
        for j in range(min(cp1, d - i)+1):
            for k in range(min(cp2, d - i - j)+1):
                l = d - i - j - k
                if l > n - cp1 - cp2 - cCommon:
                    continue
                p1 = combs[cCommon][i] * combs[cp1][j] / combs[n][d] * combs[cp2][k] * combs[n-cp1-cp2-cCommon][l]
                total += dp(cp1-j, cp2-k, cCommon-i, it * p1 if i == j == k == 0 else 1) * p1
    mem[(cp1, cp2, cCommon)] = total
    return total

print(dp(p1, p2, common))
# print(mem)