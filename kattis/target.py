class Angle:
    def __init__(self, pt, t=0):
        self.pt = pt
        self.t = t

    def t180(self):
        return Angle(-self.pt, self.t + half(self.pt))

    def cmp(self, other):
        return (self.t, half(self.pt), 0) < (other.t, half(other.pt), cross(self.pt, other.pt))

    def moveTo(self, newPt):
        otherA = Angle(newPt, self.t)
        if self.t180().cmp(otherA):
            otherA.t -= 1
        elif otherA.t180().cmp(self):
            otherA.t += 1
        return otherA

def cross(a, b):
    return (a.conjugate() * b).imag
def dot(a, b):
    return (a.conjugate()*b).real

def half(pt):
    return pt.imag < 0 or (pt.imag == 0 and pt.real < 0)

def winding(pts, o):
    mn = float("inf")
    angle = Angle(pts[-1] - o)
    for i,p in enumerate(pts):
        if onSegment(pts[i-1], pts[i], o):
            return None, None
        mn = min(mn, segToPt(pts[i-1], pts[i], o))
        angle = angle.moveTo(p - o)
    return angle.t, mn

def orient(a, b, c):
    return cross(b - a, c - a)

class Line:
    def __init__(self, a, b):
        self.v = b - a
        self.c = cross(self.v, a)
    def cmpProj(self, p, q):
        return dot(self.v, p) < dot(self.v, q)
    def side(self, p):
        return cross(self.v, p) - self.c
    def dist(self, p):
        return abs(self.side(p)) / abs(self.v)

def segToPt(a, b, p):
    line = Line(a, b)
    if line.cmpProj(a, p) and line.cmpProj(p, b):
        return line.dist(p)
    return min(abs(p - a), abs(p - b))

def onSegment(a, b, p):
    return orient(a, b, p) == 0 and dot(a - p, b - p) <= 0

it = 1
while 1:
    n = int(input())
    if not n:
        break

    points = [complex(*map(int, input().split())) for _ in range(n)]

    print(f"Case {it}")

    s = int(input())

    for _ in range(s):
        x, y = map(int, input().split())
        coords = x  + y * 1j
        res = winding(points, coords)
        if res[0] == None:
            print("Winged!")
        else:
            print("Hit!" if res[0] % 2 else "Miss!", res[1])
    it += 1

