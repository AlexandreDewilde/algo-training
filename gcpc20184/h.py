m = int(input())

if m == 1:
    print(3, 1)
    exit()
n = 3

while 2 ** (n - 1) < m:
    s = 1
    current = 1
    k = 1
    while current < m:
        k += 1
        current += k ** (n - 1)
    if current == m:
        print(n, k)
        exit()
    n += 1

print("impossible")