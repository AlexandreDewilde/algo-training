class Node:
    def __init__(self, v, prev, next):
        self.v = v
        self.next = next
        self.prev = prev

class LL:
    def __init__(self):
        self.start = None
        self.end = None

for _ in range(int(input())):
    s = input()

    l = LL()

    l.end = Node("&", None, None)
    l.start = Node("@", None, l.end)
    l.end.prev = l.start

    current = l.start
    for el in s:
        if el == "[":
            current = l.start
        elif el == "]":
            current = l.end.prev
        elif el == "<" and current != l.start:
            current.prev.next, current.next.prev = current.next, current.prev
            current = current.prev
        elif el != "<":
            ref = current.next
            current.next = Node(el, current, current.next)
            ref.prev = current.next
            current = current.next
    
    s = []
    current = l.start
    while current is not None:
        s.append(current.v)
        current = current.next
    
    print("".join(s)[1:-1])
