n,m = map(int, input().split())

s = list(map(int, input().split()))

p = list(map(int, input().split()))

r = list(map(int, input().split()))

# TIME LIMIT ERROR
def dp():
    if sum(s) == 0:
        return 0, []
    ans = float("inf")
    path = []
    for i in range(n):
        if s[i] == 0:
            continue
        for j, capa in enumerate(p):
            if p[j] < s[i]:
                continue
            peoples = s[i]
            s[i] = 0
            p[j] = 0
            res, pp = dp()
            res = res + r[j]
            if ans > res:
                path = [(i,j)] + pp
                ans = res
            s[i] = peoples
            p[j] = capa
    return ans, path

res, best = (dp())

if not best:
    print("impossible")
    exit()

ans = [0]*n
for i,j in best:
    ans[i] = j + 1
print(*ans)