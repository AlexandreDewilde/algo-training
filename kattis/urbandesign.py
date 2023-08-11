s = int(input())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, p1):
        return Point(self. x - p1.x, self.y - p1.y)

    def cross(self, p2):
        return self.x * p2.y - self.y * p2.x
    
    def cross3(self, p1, p2):
        return (p1 - self).cross(p2 - self)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.a = p2.x - p1.x
        self.b = p1.y - p2.y
        self.c = -(self.a * p1.y + self.b * p1.x)
    
    def intersect(self, line):
        den = self.a * line.b - line.a * self.b
        if den == 0:
            return None
        x = self.b * line.c - line.b * self.c
        y = self.c * line.a - line.c * self.a
        return x / den, y / den




streets = []
for _ in range(s):
    x1, y1, x2, y2 = map(int, input().split())
    streets.append(Line(Point(x1, y1), Point(x2, y2)))


t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    
    l = Line(Point(x1, y1), Point(x2, y2))
    ans = 0
    for street in streets:
        res = street.intersect(l)
        # print(res)
        if res is not None and min(x1, x2) <= res[1] <= max(x1, x2) and min(y1, y2) <= res[0] <= max(y1, y2):
            ans += 1
    
    print("different" if ans & 1 else "same")