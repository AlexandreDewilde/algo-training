x,y = input().split()

coords = {"N":0, "E":90, "S":180, "W":-90}
two_coords = {"NE": (45,"N"), "SE":(90+45,"E"), "NW":(-45,"W"), "SW":(-90-45, "S")}

def calc(s):
    if s in coords:
        return coords[s]
    
    current, up = two_coords[s[-2:]]
    dst = 22.5
    for char in s[-3::-1]:
        if char == up:
            current -= dst
        else:
            current += dst
        dst /= 2
    return current

xx = calc(x)
yy = calc(y)

# print(xx, yy)
if yy > xx:
    xx, yy = yy, xx
print(min(xx-yy, 360-xx+yy))