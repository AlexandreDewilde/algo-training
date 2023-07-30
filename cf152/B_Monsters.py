from math import ceil

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    b = [(el % k if el % k else k, -i) for i, el in enumerate(a)]

    b.sort(reverse=True)

    print(" ".join(map(str, [-i+1 for el, i in b])))