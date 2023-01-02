n = int(input())

a = list(map(int, input().split()))

b = sorted(a)
print(3)
for i in range(2):
    idx = {el:i for i,el in enumerate(a)}
    s = set()
    for j in range(n//4):
        s.add(i*n//4+j+1)
        s.add(idx[b[j+i*n//4]]+1)
    
    for j in range(n):
        if len(s) >= n//2:
            break
        s.add(j+1)
    print(*s)
    l = list(s)
    sorted_a = sorted(a[x-1] for x in s)
    for ii, j in enumerate(sorted(s)):
        a[j-1] = sorted_a[ii]
print(*range(n//2+1, n+1))