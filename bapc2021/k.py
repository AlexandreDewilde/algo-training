n,m=map(int, input().split())

l = float(input())
eps = 1e-12

if abs(l - (n**2+m**2)**0.5) < eps:
    print(2)
    print(0,0)
    print(n,m)
    exit()

def dist(p1,p2):
    return sum((x-y)**2 for x,y in zip(p1, p2))**0.5


ans = [(0,0)]
current = (0,0)

for i in range(m):
    to = (0 if i & 1 else n, current[1]+1)
    dst = dist(to, (n,m)) + n + 1

    if abs(dst - l) < eps:
        ans.append((0 if i & 1 else n, current[1]))
        ans.append((n,m))
        print(len(ans))
        for x,y in ans:
            print(x,y)
        exit()
    elif dst > l:
        break

    ans.append((0 if i & 1 else n, current[1]))
    ans.append(to)
    current = to 
    l = l - n - 1    

to = (0 if current[0] else n, current[1])
dst = dist(to, (n,m)) + n
if abs(dst-l) < eps:
    ans.append(to)
    ans.append((n,m))
    print(len(ans))
    for x,y in ans:
        print(x,y)
    exit()
elif l > dst:
    ans.append(to)
    current = to
    l -= n
dst = dist(current, (n,m))
y = m - current[1]
# if current[0] == n and dst + n - l < eps:
#     ans.append((0, current[1]))

if current[0] == 0:
    x = (l**2-y**2-n**2) / (2*l-2*n)
    ans.append((x, current[1]))
else:
    x = (l**2-y**2)/2/l
    ans.append((n-x,current[1]))
ans.append((n,m))
print(len(ans))
for x,y in ans:
    print(x,y)