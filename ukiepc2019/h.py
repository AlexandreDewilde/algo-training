c,n = map(int, input().split())

v = list(map(int, input().split()))

l = list(range(1,c+1))
l.remove(v[0])
cl = l[:]

occ = [0]*(c-1)
indices = {el:i for i,el in enumerate(l)}
current = v[0]
for i in range(1,n):
    idx = indices[v[i]]
    indices[current] = idx
    current = v[i]
    occ[idx]+= 1

sorted_idx = (sorted(enumerate(occ), key=lambda x:x[1], reverse=True))

tot = 0
for i, (j,el) in enumerate(sorted_idx):
    tot += (i+1)*el
print(tot)
print(*(cl[i] for i,_ in sorted_idx))