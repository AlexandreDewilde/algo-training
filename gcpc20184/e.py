n = int(input())
from math import gcd

def is_prime(x):
    if x <= 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
for _ in range(n):
    a,b = map(lambda x: round(float(x)*10**5), input().split())
    
    g = gcd(a,b)
    a //= g
    b //= g
    if a== b:
        print(2,2)
    elif is_prime(a) and is_prime(b):
        print(a, b)
    else:
        print("impossible")