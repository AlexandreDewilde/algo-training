n = int(input())

a = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if a[j] > 0:
            a[i] -= 1
            a[j] -= 1
            break
print("YES" if not sum(a) else "NO")