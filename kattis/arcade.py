n = int(input())

v = list(map(int, input().split()))

h = n * (n + 1) // 2
matrix = [[0] * (h + 1) for _ in range(h+1)]
b = [0] + v[:]

row = 1
for i in range(1, h+1):
    p0, p1, p2, p3, p4 = (map(float, input().split()))

    idx = i - (row - 1) * row // 2
    if p0 != 0:
        j = (row - 1) * (row - 2) // 2 + idx - 1
        matrix[i][j] += -p0
    if p1 != 0:
        j = (row - 1) * (row - 2) // 2 + idx
        matrix[i][j] += -p1
    if p2 != 0:
        j = (row + 1) * row // 2 + idx
        matrix[i][j] -= p2
    if p3 != 0:
        j = (row + 1) * row // 2 + idx + 1
        matrix[i][j] -= p3

    b[i] *= p4

    if row * (row + 1) // 2 == i:
        row += 1

b = b[1:]

matrix = matrix[1:]
for i in range(h):
    matrix[i] = matrix[i][1:]
    matrix[i][i] += 1

for i in range(h):
    for j in range(i + 1, h):
        pivot = matrix[j][i] / matrix[i][i]

        for k in range(i, h):
            matrix[j][k] -= matrix[i][k] * pivot        
        b[j] -= b[i] * pivot
for i in range(h - 1, -1, -1):
    b[i] /= matrix[i][i]
    for j in range(i):
        b[j] -= b[i] * matrix[j][i]

print(b[0])
