n = int(input())

s = set()
w = input()

s.add(w)

for i in range(1, n):
    nw = input()

    if nw in s or nw[0] != w[-1]:
        print(f"Player {1+(i&1)} lost")
        break
    s.add(nw)
    w = nw
else:
    print("Fair Game")