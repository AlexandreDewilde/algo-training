n = int(input())
ans = []

while n:
    if n < 10:
        ans.append(n)
        break
    if n == 10:
        ans.append(5)
        ans.append(5)
        break
    lm,rm = (len(str(n))+1)//2, len(str(n))//2
    left = str(n)[:lm]
    if int(left+(str(n)[:rm])[::-1]) > n:
        left = str(int(left) - 1)
    nb = int(left + (left[:rm][::-1]))
    ans.append(nb)
    n -= nb

print(len(ans))
for a in ans:
    print(a)