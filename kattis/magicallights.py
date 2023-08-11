n, q = map(int, input().split())

c = list(map(lambda x: int(x) - 1, input().split()))

p = list(map(int, input().split()))

g = [[] for _ in range(n)]
for i, el in enumerate(p):
    g[el - 1].append(i+1)


ine = [0] * n
out = [0] * n
timer = 0

stack = [(0, False)]
ine[0] = timer
timer += 1

while stack:
    x, over = stack.pop()
    if over:
        out[x] = timer
        continue
    timer += 1
    ine[x] = timer
    stack.append((x, True))
    for adj in g[x]:
        stack.append((adj, False))


t1 = [0] * (timer + 1)
t2 = [0] * (timer + 1)

def xor(i, v, t):
    while i < timer:
        t[i] ^= 1<<v
        i = i | (i + 1)

def get(i, t):
    ret = 0
    while i >= 0:
        ret ^= t[i]
        i = (i & (i + 1)) - 1
    return ret

for i, el in enumerate(c):
    if el < 50:
        xor(ine[i] - 1, el, t1)
    else:
        xor(ine[i] - 1, el - 50, t2)


for _ in range(q):
    k, x = map(int, input().split())
    k -= 1
    x -= 1
    if k == -1:
        res1 = (bin(get(out[x] - 1, t1) ^ get(ine[x] - 2, t1)).count("1"))
        res2 = (bin(get(out[x] - 1, t2) ^ get(ine[x] - 2, t2)).count("1"))
        print(res1 + res2)
    else:

        xor(ine[x] - 1, c[x] - (0 if c[x] < 50 else 50), t1 if c[x] < 50 else t2)
        xor(ine[x] - 1, k - (0 if k < 50 else 50), t1 if k < 50 else t2)
        c[x] = k