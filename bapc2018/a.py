n,x = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

ans = 0
for i in range(1,n):
    if a[i] + a[i-1] > x:
        break
    ans += 1
print(ans+1)
    