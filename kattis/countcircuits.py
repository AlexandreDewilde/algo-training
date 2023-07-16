import math

n = int(input())

ans = 0
l = [tuple(map(int, input().split())) for _ in range(n)]
s1 = {}
for mask in range(1, 1<<n//2):
    x = 0
    y = 0
    ss = []
    for i in range(21):
        if 1 << i & mask:
            y += l[i][1]
            x += l[i][0]
            ss.append(l[i])
    if x == y == 0:
        ans += 1
    if x not in s1:
        s1[x] = {y: 1}
    elif y not in s1[x]:
        s1[x][y] = 1
    else:
        s1[x][y] += 1



for mask in range(1, 1<<math.ceil(n/2)):
    x = 0
    y = 0
    for i in range(21):
        if 1 << i & mask:
            y += l[n//2 + i][1]
            x += l[n//2 + i][0]
    if x == y == 0:
        ans += 1
    if -x in s1 and -y in s1[-x]:
        ans += s1[-x][-y]

print(ans)