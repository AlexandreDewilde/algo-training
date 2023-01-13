s = input()

e = int(input())

endings = set()
for i in range(e):
    sentence = input().split()
    contain = False
    for word in sentence:
        if word == s[-len(word):]:
            contain = True
    if contain:
        for word in sentence:
            endings.add(word)
    
p = int(input())

for i in range(p):
    word = input().split()[-1]
    for i in range(len(word)):
        if word[-i:] in endings:
            print("YES")
            break
    else:
        print("NO")
    