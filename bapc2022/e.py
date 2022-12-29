n,x = map(int, input().split())

a = list(map(int, input().split()))


if sum(a) == 0:
    print(" ".join(map(str, a)))
    exit()

get = sum(el*el for el in a) / n
ans = (x / get) ** 0.5

print(" ".join(map(lambda x: str(x*ans), a)))

