from decimal import Decimal
import math
while True:
    l, n, c = map(Decimal, input().split())
    if l == n == c == -1:
        break

    if n == 0 or c == 0:
        print(0)
        continue
    lo = Decimal(0)
    hi = Decimal(math.pi) * 2

    while hi - lo > 1e-14:
        mid = (hi + lo) / 2

        f = Decimal(math.sin(mid / 2))
        if f * 2 < mid / (1 + n * c):
            hi = mid
        else:
            lo = mid

    # print(mid)

    r = (1 + n * c) * l / lo
    print(round(r*(1 - Decimal(math.cos(lo/2))), 3))