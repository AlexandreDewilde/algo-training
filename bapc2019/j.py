n = int(input())

for m in range(2,n):
    mn = m*n
    k = 2
    while k*k <= mn:
        if mn % (k*k) == 0:
            break
        k += 1
    else:
        print(m)
        break
    