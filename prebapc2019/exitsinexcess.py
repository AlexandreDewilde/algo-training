n, m = map(int, input().split())

l, r = [], []
for i in range(m):
    u,v = map(int, input().split())
    if u > v:
        l.append(str(i + 1))
    else:
        r.append(str(i + 1))

print(min(len(l), len(r)))

print("\n".join(l if len(l) < len(r) else r))
    