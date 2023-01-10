n = int(input())


scores = {"red":1, "yellow":2, "green":3, "brown":4, "blue":5, "pink":6,"black":7}

total = 0
red = 0
mx = 0
for i in range(n):
    color = input()
    if color == "red":
        red += 1
    else:
        mx = max(mx, scores[color])
        total += scores[color]

if red == n:
    print(1)
else:
    print(mx*red+red+total)
