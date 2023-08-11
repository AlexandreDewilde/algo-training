n, m, k = map(int, input().split())

a = list(map(int, input().split()))

a = sorted(enumerate(a), key=lambda x: x[1])

if k % m or k == 0:
    print("impossible")
    exit()
p = k // m

zeros = n - p - 1
ones = n - p
ans = []

current = 0
it = 0
while zeros >= 0 or ones < n:
    if ones < n and current <= a[ones][1] * it:
        current += m
        ans.append(a[ones][0] + 1)
        ones += 1
    elif zeros >= 0 and current > a[zeros][1] * it:
        ans.append(a[zeros][0] + 1)
        zeros -= 1
    else:
        print("impossible")
        exit()
    it += 1

print(" ".join(map(str, ans)))