import heapq
n,k = map(int, input().split())

current = {}
for _ in range(n):
    name, s = input().split()
    s = int(s)
    current[name] = s

l = int(input())
occ = {}
mx = {}
for _ in range(l):
    name, s = input().split()
    s = int(s)
    occ[name] = occ.get(name, 0) + 1
    if mx.get(name, (0,0))[0] == s:
        mx[name] = mx.get(name, (0,0))
        mx[name] = (mx[name][0], mx[name][1]+1)
    
    elif mx.get(name, (0,0))[0] <s:
        mx[name] = (s, 1)

    if current[name] < s:
        add = (s-current[name])
        k -= add
        current[name] += add

if k < 0:
    print(0)
    exit()
pq = []
score = 0
lst = []
for name, m in mx.items():
    if current[name] > m[0]:
        score += current[name]*occ[name]
        lst.append((-occ[name],False))
    else:
        score += current[name]*(occ[name]-mx[name][1])
        lst.append((-(occ[name]+mx[name][0]*mx[name][1]), True))
        lst.append((-occ[name], False))


lst.sort()
i = 0
while k > 0:
    add, limited = lst[i]
    if not limited:
        score -= add*k
        break
    score -= add
    i += 1

    k -= 1

print(score)