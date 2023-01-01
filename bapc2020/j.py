cc,e,m = map(int, input().split())

if cc != 4:
    print("impossible")
    exit()
if e == 0 == m:
    print(2,2)
    exit()

a,b,c = 1, -e/2, m
rho = b**2 - 4*a*c
h=w=0
if rho < 0:
    print("impossible")
    exit()
elif rho == 0:
    h = int(-b/2/a)
    if h != 0:
        h,w = (h+2,m//h+2)
else:
    h1, h2 = int((-b + rho**0.5) / 2 / a),int((-b - rho**0.5) / 2 / a)
    if h1 != 0:
        h,w = h1+2, m//h1+2
    if h2 != 0 and h*w != e+cc+m:
        h,w = h2 + 2, m//h2 + 2
      
if h*w == cc+e+m:
    print(h,w)
else:
    print("impossible")