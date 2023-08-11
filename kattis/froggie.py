l, w = map(int, input().split())


cars = []
for _ in range(l):
    o, i, s = map(int, input().split())
    cars.append((o, i, s))
p, s = input().split()

p = int(p)

pos = [-1, p]
for it, el in enumerate(s):    
    if 0 <= pos[0] < l:
        o, i, s = cars[l - pos[0] - 1]

        res = (o + s * it)
        # print(pos, (res % 2 if (l - pos[0] - 1) % 2 == 0 else (w - res - 1) % i), pos[1] % i)
        if  pos[1] % i == (res % i if (l - pos[0] - 1) % 2 == 0 else (w - res - 1) % i):
            print("squish")
            exit()
    # print()
    if el == "U":
        pos[0] += 1
    elif el == "D":
        pos[0] -= 1
    
    elif el == "L":
        pos[1] -= 1

    else:
        pos[1] += 1

    
print("safe" if pos[0] >= l else "squish")
