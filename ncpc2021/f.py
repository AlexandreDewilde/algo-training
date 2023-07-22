n, k, p = input().split()

p = float(p)
n = int(n)
k = int(k)

nb = [i for i in range(1<<n) if bin(i).count("1") < k]

pos = [float("inf") for i in range(1<<n)]
for i, el in enumerate(nb):
    pos[el] = i

mat = [[0]*len(nb) for _ in range(len(nb))]
b = [0] * len(nb)

for i, el in enumerate(nb):

    mat[i][i] = 1
    b[i] = 1
    mat[i][pos[(el<<1)&~(1<<n)]] -= 1 - p
    if pos[((el<<1)&~(1<<n))|1] != float("inf"):
        mat[i][pos[((el<<1)&~(1<<n))|1]] -= p

for i in range(len(mat)):
    for j in range(i + 1, len(mat)):
        fac = mat[j][i] / mat[i][i]
        for k in range(len(mat)):
            mat[j][k] -= fac * mat[i][k]
        b[j] -= fac * b[i]
for i in range(len(mat) - 1, -1, -1):
    b[i] /= mat[i][i]
    for j in range(i):
        b[j] -= mat[j][i] * b[i]
print(b[0])