import sys
n, q = map(int, sys.stdin.readline().split())

class Node:
    def __init__(self, v, prev, next):
        self.v = v
        self.next = next
        self.prev = prev

class LL:
    def __init__(self):
        self.begin = None
        self.end = None


mappings = {}
l = LL()
l.begin = Node(0, None, None)
current = l.begin
pos = [None] * (2 * n)
pos[0] = current
for i in range(1, 2 * n):
    current.next = Node(i, current, None)
    current = current.next
    pos[i] = current
l.end = current

partners = {}
for _ in range(n):
    s1, s2 = sys.stdin.readline().split()
    mappings[s1] = len(mappings)
    mappings[s2] = len(mappings)
    partners[mappings[s1]] = mappings[s2]
    partners[mappings[s2]] = mappings[s1]

rev_map = {v: k for k, v in mappings.items()}

def print_ll(l):
    current = l.begin
    i = 0
    d = []
    while current != None and i < 2 * n:
        d.append(current.v)
        current = current.next
        i += 1
    print("\n".join(rev_map[i] for i in d))

q = sys.stdin.readline().replace("\n", "")

ans = []
current = l.begin
for el in q:
    if el == "F":
        current = current.prev
    elif el == "B":
        
        current = current.next
    elif el == "R":
        if current == l.end:
            current = l.begin
        else:
            if current == l.begin:
                l.begin = current.next
            next = current.next
            if current.prev is not None:
                current.prev.next, current.next.prev = current.next, current.prev
            else:
                current.next.prev = current.prev
            current.prev = l.end
            l.end.next = current
            current.next = None
            l.end = current
            current = next
    elif el == "C":
        if current == l.end:
            current.prev.next = None
            l.end = current.prev
            goto = pos[partners[current.v]]
            goto.next, current.next, current.prev, goto.next.prev = current, goto.next, goto, current
            if goto == l.end:
                l.end = current
            current = l.begin
        else:
            if current == l.begin:
                l.begin = current.next
            next = current.next
            if current.prev is not None:
                current.prev.next, current.next.prev = current.next, current.prev
            else:
                current.next.prev = current.prev
            goto = pos[partners[current.v]]
            if goto.next is not None:
                current.next, goto.next.prev = goto.next, current
            else:
                current.next = goto.next
            goto.next = current
            current.prev = goto
            if goto == l.end:
                l.end = current
            current = next
    else:
        ans.append(partners[current.v])

print("\n".join(rev_map[i] for i in ans) + "\n")
print_ll(l)