n = int(input())

c = list(map(int, input().split()))

print(sum(1/el if el != 0 else 2 for el in c))