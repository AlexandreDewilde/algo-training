for _ in range(int(input())):
    n, C = map(int, input().split())
    
    l = list(map(int, input().split()))
    s2 = sum(el**2 for el in l)
    s = sum(l)

    a = n * 4
    b = 4 * s
    c = s2 - C

    rho = b ** 2 - 4 * a * c
    print((-b + int(rho**0.5)) // (2 * a))
