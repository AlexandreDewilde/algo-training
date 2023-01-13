from functools import cmp_to_key
s = input()

occ = {}
for el in map(int, list(s)):
    occ[el] = occ.get(el,0)+1


for i in range(1, 10):
    if i not in occ:
        print(i)
        exit()
if 0 not in occ:
    print(min(occ)*10)
    exit()

def compare(x,y):
    if x[1] != y[1]:
        return x[1] - y[1]
    xx,yy = x[0],y[0]
    if x[0] == 0:
        xx = float("inf")
    if y[0] == 0:
        yy = float("inf")
    return xx-yy

res = min((occ.items()), key=cmp_to_key(compare))
if res[0] == 0:
    print('1'+'0'*(res[1]+1))
    exit()
print(str(res[0])*(res[1]+1))