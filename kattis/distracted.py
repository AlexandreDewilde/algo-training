n, l = map(int, input().split())


married = {}

for _ in range(n):
    name, m = input().strip().split()

    married[name] = m

ans = 0
for _ in range(l):
    n1, n2 = input().strip().split(" -> ")

    if married[n1] == "m" and married[n2] == "u":
        ans = 1
    
    elif ans != 1 and (married[n1] in {"m", "?"} and married[n2] in {"u", "?"}):
        ans = "?"
    
    

print(ans)
