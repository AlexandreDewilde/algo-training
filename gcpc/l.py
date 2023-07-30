s = input()

cnt = 0
for i, c in enumerate(s):
    cnt += 1 if c == "(" else -1
    if cnt == 0:
        break
ans = s[i+1:] + s[:i+1]
print(ans if ans != s else "no")