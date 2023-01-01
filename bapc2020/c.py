n,p = map(int, input().split())

teams = []
for _ in range(n):
    t = int(input())
    teams.append(t)
if sum(teams) == 0:
    for team in teams:
        print(0)
    exit()

teams.append(0)
current = p 
ans = [p]
for i in range(1,n+1):
    if teams[i] < teams[i-1]:
        p -= 1
    ans.append(p)

if p != 0:
    print("ambiguous")
else:
    for a in ans[:-1]:
        print(a)