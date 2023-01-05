n = int(input())

s = input()
line = [ord(c)-ord('A') for c in s]

a = s.count("A")
b = s.count("B")
c = s.count("C")


ans = n + 1
for _ in range(2):
    cnt = [[0]*3 for _ in range(3)]
    for i in range(a):
        cnt[0][line[i]] += 1
    for i in range(a, a+b):
        cnt[1][line[i]] += 1
    for i in range(a+b, n):
        cnt[2][line[i]] += 1
    
    for i in range(n):
        ans = min(ans, n - cnt[0][0] - cnt[1][1] - cnt[2][2])
        cnt[0][line[i]] -= 1
        cnt[1][line[(i+a)%n]] -= 1
        cnt[2][line[(i+a+b)%n]] -= 1
        cnt[0][line[(i+a)%n]] += 1
        cnt[1][line[(i+a+b)%n]] += 1
        cnt[2][line[i]] += 1
    line.reverse()
print(ans)

        