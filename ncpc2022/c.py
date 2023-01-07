n = int(input())

s = list(input())
sc = s[:]
for i in range(n-1):
    if sc[i] == "1":
        s[i+1] = "1"
        if i + 2 < n:
            s[i+2] = "1"

print(sum(map(int, s)))