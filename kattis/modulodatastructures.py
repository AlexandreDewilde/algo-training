n, q = map(int, input().split())

array = [0] * (n + 1)
size = int(n ** 0.5) + 1
decomp = [[0]*size for _ in range(size)]

for _ in range(q):
    s = input()

    if s[0] == "1":
        _, a, b, c = map(int, s.split())
        if b < size:
            decomp[b][a] += c
        else:
            i = a
            while i <= n:
                array[i] += c
                i += b

    else:
        _, d = map(int, s.split())

        ans = 0
        for i in range(1, size):
            ans += decomp[i][d%i]
        print(ans + array[d])