import sys
input = sys.stdin.readline

n,x = map(int, input().split())

base = 1 << (n-1)
if base > x:
    print("impossible")
    exit()

line = [1]*n
line[0] += x - base
ans = [line]

for i in range(n-1, 0, -1):
    new_line = []
    for j in range(1, i+1):
        new_line.append(line[j-1]+line[j])
    ans.append(new_line)
    line = new_line
for row in ans[::-1]:
    print(*row)