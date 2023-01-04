v = int(input())

i = 1
ans = float("inf")
while i * i <= v:
    j = 1

    while j * j <= v:
        if v % (i*j) == 0:
            ans = min(ans, 2*(i*j+v//i+v//j))
        j += 1
    i += 1
print(ans)