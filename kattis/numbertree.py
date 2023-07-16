inp = input()
if len(inp.split()) == 1:
    n = inp
    path = ""
else:
    n, path = inp.split()
n = int(n)

start = 0
for i in range(n - len(path)):
    start += 2 ** (n - i)

diff = 0
for i, el in enumerate(path[::-1]):
    if el == "L":
        diff += 2 ** i
print(start + diff + 1)