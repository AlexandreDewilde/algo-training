n = int(input())

m = list(map(int, input().split()))

one = [i+ 1 for i, el in enumerate(m) if el == 1]
if len(one) >= 2:
    print(one[0], one[1])
    exit()
pres = set(m)
mx = max(m)

x = y = 1

while x <= mx:
    x, y = x + y, x
    if x != y != 1 and x in pres and y in pres:
        print(m.index(y) + 1, m.index(x) + 1)
        exit()

print("impossible")