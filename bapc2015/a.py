import math

def calc(k, wagons, n):
    l = 1
    start = 1
    if wagons[0] > k:
        l = 2
        start = wagons[0]
    for i in range(len(wagons)):
        if wagons[i] >= start + 2 * k:
            l += 2
            start = wagons[i]
        elif wagons[i] >= start + k:
            l += 1
            start += k
    if n >= start + k:
        l += 1
    return l

for _ in range(int(input())):
    n, w, L = map(int, input().split())
    
    wagons = list(map(int, input().split()))
    wags = []
    if wagons[0] != 1:
        wags.append(0)
        wags.append(wagons[0] - 1)

    l = -1

    r = n

    while r - l > 1:
        mid = l + (r - l) // 2
        if calc(mid, wagons, n) > L:
            l = mid
        else:
            r = mid
    print(l + 1)