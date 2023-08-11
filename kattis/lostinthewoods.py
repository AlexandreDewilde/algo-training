n, m = map(int, input().split())

mat = [[0]*(n) for _ in range(n)]


for _ in range(m):
    a, b = map(int, input().split())
    mat[a][b] = 1
    mat[b][a] = 1

for i in range(n):
    s = sum(mat[i])
    for j in range(n):
        mat[i][j] =  -mat[i][j] / s

for i in range(n):
    mat[i][i] = 1


b = [1] * (n - 1)

for i in range(n - 1):
    for j in range(i + 1, n - 1):
        pivot = mat[j][i] / mat[i][i]
        for k in range(i, n - 1):
            mat[j][k] -= mat[i][k] * pivot
        b[j] -= b[i] * pivot

for i in range(n - 2, -1, -1):
    b[i] /= mat[i][i]
    for j in range(i):
        b[j] -= b[i] * mat[j][i]

print(b[0])