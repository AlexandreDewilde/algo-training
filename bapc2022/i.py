from collections import defaultdict, deque

n,q  = map(int, input().split())

mappings = {}
g = [[] for _ in range(2*n)]
for _ in range(n):
    _, unit, _, val, unit_2 = input().split()
    if unit not in mappings:
        mappings[unit] = len(mappings)
    if unit_2 not in mappings:
        mappings[unit_2] = len(mappings)
    g[mappings[unit]].append((float(val), mappings[unit_2]))
    g[mappings[unit_2]].append((1/float(val), mappings[unit]))

def bfs(x):
    ratio = [float("inf")]*len(mappings)
    ratio[x] = 1
    q = deque([x])
    while q:
        u = q.popleft()
        for val, v in g[u]:
            if ratio[v] == float("inf"):
                ratio[v] = ratio[u] * val
                q.append(v)
    return ratio
ratios = [bfs(i) for i in range(len(mappings))]
for _ in range(q):
    x, u1, _, u2 = input().split()
    ans = (ratios[mappings[u1]][mappings[u2]])
    if ans == float("inf"):
        print("impossible")
    else:
        print(ans*float(x))