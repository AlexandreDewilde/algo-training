import sys
input = sys.stdin.readline

n, c = map(int, input().split())

w = list(map(int, input().split()))

w.sort(reverse=True)

i = 0
ans = 0
while i < len(w):
    if i != len(w) - 1 and w[i] + w[-1] <= c:
        w.pop()
    ans += 1
    i += 1
    
print(ans)