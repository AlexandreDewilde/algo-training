from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = n
    pres = {}
    for i in range(n):
        new_pres = {}
        for k, v in pres.items():
            ans = max(ans, (i - v) * k)
            g = gcd(k, a[i])
            new_pres[g] = min(new_pres.get(g, float("inf")), v)
        new_pres[a[i]] = min(new_pres.get(a[i], float("inf")), i)
        pres = new_pres
    
    for k, v in pres.items():
        ans = max(ans, (n - v) * k)
    print(ans)