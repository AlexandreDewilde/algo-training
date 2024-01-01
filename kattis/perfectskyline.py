n, s = map(int, input().split())

blocks = list(map(int, input().split()))

buildings = list(map(int, input().split()))

dp = [[-1]*2**n for _ in range(s+1)]

dp[0][2**n-1] = 2**n-1

for i in range(s):
    for av in range(2**n):
        if dp[i][av] == -1:
            continue

        mask = av
        while mask:
            mask = (mask-1) & av

            total = 0
            for j in range(n):
                if (av & (1<<j)) and not (mask & (1<<j)):
                    total += blocks[j]
            if total == buildings[i]:
                dp[i+1][mask] = av

start = next(((el,i) for i, el in enumerate(dp[s]) if el != -1), -1)
if start == -1:
    print(-1)
    exit()

ans = []

current, prev = start
for i in range(s-1, -1,-1):
    ret = []
    for j in range(n):
        if not (prev & (1<<j)) and (current & (1 << j)):
            ret.append(j+1)
    ans.append(ret)
    prev = current
    current = dp[i][current]

for l in ans[::-1]:
    print(len(l), *l)