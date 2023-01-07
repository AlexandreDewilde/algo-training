n = int(input())
h = list(map(int, input().split()))

new_h = [h[0]]
for i in range(1,n):
    if h[i] != new_h[-1]:
        new_h.append(h[i])

l = r = high = h[0]
h =new_h
ans = 0
for i in range(1,len(h)):
    if h[i] >= h[i-1]:
        high = h[i]
    r = h[i]
    ans = max(ans,high-max(l,r))
    if i+1 < len(h) and h[i-1] > h[i] < h[i+1]:
        l = h[i]
print(ans)