from math import ceil

def euclidian(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = euclidian(b, a % b)
    
    return y, x - y * (a // b), d

for _ in range(int(input())):
    r, s, q = map(int, input().split())
    
    x, y, d = euclidian(r, -s)
    y = -y
    x *= q // d
    y *= q // d

    k = (max(ceil((1-x)/(-s//d)), ceil((1-y)/(r//d))))
    print(x - k * (s // d), y + k * (r // d))

