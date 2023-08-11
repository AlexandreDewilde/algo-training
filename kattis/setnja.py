s = input()

ans = 1
b = 1

for el in s:
    if el == "L":
        ans = 2 * ans
    
    elif el == "R":
        ans = 2 * ans + b
    
    elif el == "*":
        ans = 2 * ans + 2 * ans + b + ans
        b *= 3

print(ans)