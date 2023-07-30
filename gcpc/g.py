n = int(input())

if n // 10 == 0:
    print(n + 1)

else:
    ans = (len(str(n)) - 1) * 10
    last = int(str(n)[0])
    prev = int(str(n)[1])

    if prev > last or (prev == last and int(str(last) * len(str(n))) <= n):
        ans += last
    else:
        ans += last - 1

    print(ans)