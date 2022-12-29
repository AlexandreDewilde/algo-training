n = int(input())

workers = []
for _ in range(n):
    b,p = map(int, input().split())
    workers.append((b,p))

workers.sort()

if n%2:
    print("impossible")
    exit()
target = (workers[-1][0]+workers[0][0], workers[0][1]+workers[-1][1])
for i in range(n//2):
    if target != (workers[n-i-1][0]+workers[i][0], workers[i][1]+workers[n-i-1][1]):
        print("impossible")
        break
else:
    print("possible")