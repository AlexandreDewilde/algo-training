import heapq

n,m = map(int, input().split())

s = list(map(int, input().split()))

p = list(map(int, input().split()))

r = list(map(int, input().split()))

class Node:
    def __init__(self, cost, capa, pos=None):
        self.cost = cost
        self.capa = capa
        self.pos = pos
    def get(self):
        return self.cost

class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [Node(float("inf"), i) for i in range(n*4)]
    
    def add(self, v, tl, tr, pos, val, position):
        if tl == tr:
            self.tree[v] = Node(val, pos, position)
        else:
            mid = (tl+tr) // 2
            if pos <= mid:
                self.add(v*2, tl, mid, pos, val, position)
            else:
                self.add(v*2+1, mid+1, tr, pos, val, position)
            if self.tree[v*2].get() < self.tree[v*2+1].get():
                self.tree[v] = self.tree[v*2]
            else:
                self.tree[v] = self.tree[v*2+1]
    

    def get_min(self, v, tl, tr, l, r):
        if l > r:
            return Node(float("inf"), float("inf"))
        
        if (l == tl and r == tr):
            return self.tree[v]
        mid = (tl+tr) // 2
        ret1 = self.get_min(v*2, tl, mid, l, min(r, mid))
        ret2 = self.get_min(v*2+1, mid+1, tr, max(l, mid+1), r)

        if ret1.get() < ret2.get():
            return ret1
        return ret2
    def min(self, l):
        return self.get_min(1, 0, self.n-1, l, self.n-1)
    
    def rm(self, pos):
        self.add(1, 0, self.n-1, pos, float("inf"), 0)

tree = SegTree(max(p)+1)
nodes = {}
for i in range(m):
    if p[i] in nodes:
        heapq.heappush(nodes[p[i]], (r[i], i))
    else:
        nodes[p[i]] = [(r[i], i)]
    
for k, val in nodes.items():
    cost, pos = heapq.heappop(nodes[k])
    tree.add(1, 0, tree.n-1, k, cost, pos)

ans = [0]*n
for i, el in sorted(enumerate(s), key=lambda x: x[1], reverse=True):
    node = tree.min(el)
    if node.cost == float("inf"):
        print("impossible")
        exit()
    tree.rm(node.capa)
    if len(nodes[node.capa]):
        cost, pos = heapq.heappop(nodes[node.capa])
        tree.add(1,0,tree.n-1, node.capa, cost, pos)
    ans[i] = node.pos + 1
print(*ans)