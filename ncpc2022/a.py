n = int(input())

scores = []
for i in range(n):
    x,y = map(int, input().split("-"))
    scores.append((x,y))

if scores[0] == (11,11):
    print(f"error 1")
    exit()

for i in range(1,n):
    if scores[i] == scores[i-1]:
        continue
    
    prev_serv = ((sum(scores[i-1])+1) // 2) % 2
    serv = ((sum(scores[i])+1) // 2) % 2
  
    if sum(scores[i-1]) >= sum(scores[i]) or (max(scores[i-1]) == 11) or (scores[i] == (11,11)):
        print(f"error {i+1}")
        break
    if serv == prev_serv and (scores[i][0] < scores[i-1][0] or scores[i][1] < scores[i-1][1]):
        print(f"error {i+1}")
        break
    elif serv != prev_serv and (scores[i][0] < scores[i-1][1] or scores[i][1] < scores[i-1][0]):
        print(f"error {i+1}")
        break
else:
    print("ok")