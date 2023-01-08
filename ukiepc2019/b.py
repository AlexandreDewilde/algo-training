n = int(input())

np = n
nb = 0
last = 0
while np:
    nb += 1
    last = np
    np //= 10

up = (last+1)*10**(nb-1)
down = (last)*10**(nb-1)
if abs(n-up) <= abs(n-down):
    print(up)
else:
    print(down)

