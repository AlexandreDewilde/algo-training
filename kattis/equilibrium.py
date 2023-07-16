n = int(input())

for _ in range(n):
    weights = {}

    s = input()
    tot = 0

    opened = 0
    current = 0
    for el in s:
        if el == "[":
            opened += 1
        elif el == "]":
            if current:
                tot += 1
                weights[current * 2 ** opened] = weights.get(current * 2 ** opened, 0) + 1
                current = 0
            opened -= 1
        elif el == ",":
            if current:
                tot += 1
                weights[current * 2 ** opened] = weights.get(current * 2 ** opened, 0) + 1
                current = 0
        else:
            current = current * 10 + int(el)
    if current:
        tot += 1
        weights[current] = 1
    print(tot - max(weights.values()))
