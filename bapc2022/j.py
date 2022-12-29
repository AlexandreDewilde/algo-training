import random

w,h = map(int, input().split())

x = 1
m = 1
ans = (1,0)
l = list(range(1, w+1))
random.shuffle(l)
for i in l:
    print(f"? {i} {min(m, h)}")
    res = input()
    
    if res == "sky":
        continue

    lo = m + 1
    hi = h + 1
    while hi > lo:
        mid = (lo+hi) // 2
        print(f"? {i} {mid}")
        res = input()
        if res == "building":
            lo = mid + 1
        else:
            hi = mid
    x,m = i,hi


print(f"! {x} {m-1}")
