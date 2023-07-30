import math

n = int(input())
if n == 1:
    print(1, 0)
    exit()

for a in range(1, math.ceil(math.sqrt(n))):
    if n % a == 0:
        b = n // a
        m = (a + b) // 2
        k = (b - a) // 2
        if m ** 2 - k ** 2 != n or m < 0 or k < 0:
            continue
        print(m, k)
        exit()

print("impossible")