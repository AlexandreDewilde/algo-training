n, c = map(int, input().split())

l = list(map(int, input().split()))

smallest = l[0]
biggest = l[0]

ans = []
for i in range(n):

    smallest = min(smallest + c, l[i])
    biggest = max(biggest - c, l[i])
    ans.append(max(-(l[i] - biggest), (l[i] - smallest)))

print(" ".join(map(str, ans)))