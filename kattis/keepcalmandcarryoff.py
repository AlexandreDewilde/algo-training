a = input()
b = input()

if len(a) < len(b):
    a, b = b, a
b = "0" + "0" * (len(a) - len(b) + 1) + b
a = "00" + a

def solve(a,b):
    idx = -1

    for i in range(len(a)):
        if int(a[i]) + int(b[i]) >= 10:
            idx = i
            break
    
    if idx == -1:
        print("0")
        exit()
    
    idx -= 1
    while idx > 0 and int(a[idx]) + int(b[idx]) == 9:
        idx -= 1
    
    ans = [0] * (len(a[idx+1:]) + 1)
    ans[-1] = 1
    # print(a[idx+1:])
    for i, el in enumerate(a[idx+1:][::-1]):
        ans[i] -= int(el)
        while ans[i] < 0:
            ans[i + 1] -= 1
            ans[i] += 10
        # print(ans)
    return ans[::-1]

res = min(solve(a,b), solve(b, a))
print("".join(map(str, res)).lstrip("0"))