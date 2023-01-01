n = int(input())

for _ in range(n):
    nb, *l = input().split()
    
print(nb)
for i in range(int(nb)):
    print(l[i])