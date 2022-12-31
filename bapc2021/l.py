#based on jury solutions

n = int(input())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
    
sorted_mat = sorted(enumerate(list(sum(mat[i]) for i in range(n))), key=lambda x:x[1])


score = 0
for i in range(n//2):
    score -= sorted_mat[i][1]
for i in range(n//2, n):
    score += sorted_mat[i][1]
    
print(score//2)