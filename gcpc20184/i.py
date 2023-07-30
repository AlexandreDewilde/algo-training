n = int(input())


h = list(map(int, input().split()))

v = list(map(int, input().split()))

ans = max(0 ,v[0] - h[0])

h = [h[i] + ans for i in range(n)]

greater = False
for a, b in zip(h, v):
    if b > a:
        print(ans + 1)
        exit()
    elif a > b:
        break
print(ans)