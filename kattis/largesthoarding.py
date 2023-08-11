n = int(input())

buildings = [tuple(map(int, input().split())) for _ in range(n)]

stack = []

ans = 0
for i in range(n):
    width = 0
    while stack and stack[-1][0] > buildings[i][0]:
        h, w = stack.pop()
        width += w
        ans = max(ans, h * width)
    
    stack.append((buildings[i][0], width + buildings[i][1]))

width = 0
while stack:
    h, w = stack.pop()
    width += w
    ans = max(ans, h * width)
print(ans * 50)