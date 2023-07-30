n,h,w = map(int, input().split())

for _ in range(n):
    g,b = input().split()
    ans = ["N", "N"]
    if g == "Y" or w == 0:
        ans[0] = "Y"
        w += 1
        h -= 1
    
    if b == "Y" or h == 0:
        h += 1
        w -= 1
        ans[1] = "Y"
    
    print(" ".join(ans))