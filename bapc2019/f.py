k = int(input())

class Fenwick:
    def __init__(self,n):
        self.n = n
        self.array = [0]*n
    def sum(self, r):
        if r == -1:
            return 0
        ret = 0
        while r >= 0:
            ret += self.array[r]
            r = (r & (r+1)) - 1
        return ret
    def add(self, idx):
        while idx < self.n:
            self.array[idx] += 1
            idx = idx | (idx+1)
            

ans = []
for pic in range(k):
    n = int(input())
    h = list(map(int, input().split()))
    tree = Fenwick(n)
    mx_idx = -1
    for i, j in sorted(enumerate(h), key=lambda x: x[1], reverse=True):
        mx_idx = max(i, mx_idx)
        tree.add(i)
        if mx_idx > i and tree.sum(mx_idx) - tree.sum(i-1) < mx_idx - i + 1:
            ans.append(pic+1)
            break

print(len(ans))
print(*ans, sep="\n")