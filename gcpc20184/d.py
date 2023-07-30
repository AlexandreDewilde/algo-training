n = int(input())

a = list(map(int, input().split()))

b = [0]

for el in a:
    b.append(el - b[-1])

odd = b[1]
even = b[0]
for i in range(len(b)):
    if i & 1:
        odd = min(odd, b[i])
    else:
        even = min(even, b[i])

print(max(0, odd + even + 1))