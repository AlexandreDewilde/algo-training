c = float(input())

l = int(input())

total = 0
for i in range(l):
    
    w, l = map(float, input().split())
    total += w*l

print(total*c)
