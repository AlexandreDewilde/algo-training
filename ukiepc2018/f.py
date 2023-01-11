n = int(input())

s = list(map(int, input().split()))
    
fib = [0]*50
fib[0] = fib[1] = 1

for i in range(2, len(fib)):
    fib[i] = fib[i-1] + fib[i-2]

occ = {float("inf"): float("inf")}

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.current_n = 0
        self.array = [float("inf")]*(2*n)
        self.pos = {}
    def full(self):
        return self.current_n >= self.n
    
    def get_min(self):
        return self.min(0, self.n)

    def min(self, i, j):
        i += self.n
        j += self.n
        res = float("inf")
        while i < j:
            if i % 2 == 1:
                res = min(res, self.array[i], key=lambda x:occ[x])
                i += 1
            if j % 2 == 1:
                j -= 1
                res = min(res, self.array[j], key=lambda x:occ[x])
            
            i //= 2
            j //= 2
        return res

    def update(self, pos, val):
        pos += self.n
        self.array[pos] = val
        while pos > 1:
            pos //= 2
            self.array[pos] = min(self.array[pos*2], self.array[pos*2+1], key=lambda x: occ[x])
        

    def add(self, val):
        self.update(self.current_n, val)
        self.pos[val] = self.current_n
        self.current_n += 1

    
    def replace(self, prev_val, val):
        self.update(self.pos[prev_val], val)
        self.pos[val] = self.pos[prev_val]
        # del self.pos[prev_val]
 
blocks = [SegmentTree(fib[0])]
ans = 0
index = {}
lst = []
for el in s:
    if el not in occ:
        occ[el] = 0
        if blocks[-1].full():
            blocks.append(SegmentTree(fib[len(blocks)]))
        blocks[-1].add(el)
        index[el] = len(blocks) - 1
    
    ans -= occ[el]*(index[el]+2)
    occ[el] += 1

    current = index[el]
    blocks[current].replace(el, el)
    while current >= 1 and occ[blocks[current-1].get_min()] < occ[el]:
        prev_min = blocks[current-1].get_min()
        blocks[current-1].replace(prev_min, el)
        blocks[current].replace(el, prev_min)
        ans += occ[prev_min]
        index[prev_min] = current
        index[el] = current - 1
        current -= 1
    ans += occ[el]*(current+2)
    lst.append(ans)
print(*lst,sep="\n")


