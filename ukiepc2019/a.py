import sys
input = sys.stdin.readline

s = int(input())

slots = []
mx_w = 0
for i in range(s):
    a,b = map(int, input().split())
    slots.append((a,b,i+1))
    mx_w = max(mx_w, b)

c = int(input())
coins = []
for i in range(c):
    u,v = map(int, input().split())
    coins.append((u,v))
    mx_w = max(mx_w, v)

slots.sort()
coins.sort(reverse=True)

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.array = [float("inf")]*n
    
    def add(self, idx, val):
        while idx < self.n:
            self.array[idx] = min(self.array[idx], val)
            idx = idx | (idx+1)

    def min(self, r):
        ans = float("inf")
        while r >= 0:
            ans = min(ans, self.array[r])
            r = (r & (r+1)) - 1
        return ans
tree = Fenwick(mx_w+1)
ans = 0
for i in range(c):
    while slots and slots[-1][0] >= coins[i][0]:
        slot = slots.pop()
        tree.add(slot[1], slot[2])
    ans += tree.min(coins[i][1])
print(ans)
