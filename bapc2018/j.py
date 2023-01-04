a,b,c,d = map(int, input().split())

p = (a+b+c+d) / 2

s = ((p-a)*(p-b)*(p-c)*(p-d))**0.5
print(s)