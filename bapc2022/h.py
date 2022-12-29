n = int(input())

g = [[] for _ in range(n)]

for i in range(n):
    u,v,h = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v,h,i))
    g[v].append((u,h,i))



start_street = [-1]*n

def dfs(x, start=False):
    values = [set() for _ in range(n)]
    used = set()
    stack = [x]
    while stack:
        x = stack.pop()
        for adj, h, i in g[x]:
            if (adj, x) in used or (x,adj) in used:
                continue
            used.add((x,adj))
            if not start:
                if 1 not in values[x] and h not in values[adj]:
                    values[x].add(1)
                    values[adj].add(h)
                    start_street[i] = x
                elif h not in values[x] and 1 not in values[adj]:
                    values[x].add(h)
                    values[adj].add(1)
                    start_street[i] = adj
                else:
                    return False
            else:
                if h not in values[x] and 1 not in values[adj]:
                    values[x].add(h)
                    values[adj].add(1)
                    start_street[i] = adj
                elif 1 not in values[x] and h not in values[adj]:
                    values[x].add(1)
                    values[adj].add(h)
                    start_street[i] = x
                else:
                    return False

            stack.append(adj)
    return True

start = 0
for i in range(n):
    if len(g[i]) <= 2:
        start = i
        break

res = dfs(start)
if not res:
    res = dfs(start, True)
if not res:
    print("impossible")
    exit()

for start in start_street:
    print(start+1)