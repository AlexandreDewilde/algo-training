n = int(input())

aa = list(map(int, input().split()))

aa.sort(reverse=True)

a = b =0

for i, el in enumerate(aa):
    if i & 1:
        b += el
    else:
        a += el
print(a, b)