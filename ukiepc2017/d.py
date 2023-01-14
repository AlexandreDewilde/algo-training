from collections import defaultdict
s = list(input())

#based on jury solutions
pos = defaultdict(set)

for i,el in enumerate(s): pos[el].add(i)


start = defaultdict(set)

s.sort()
for i, el in enumerate(s):
    start[el].add(i)

for k in sorted(start.keys()):
    good = start[k] & pos[k]
    
    diff_a = sorted(pos[k] ^ good)
    diff_b = sorted(start[k] ^ good)

    for a, b in zip(diff_a, diff_b):
        
        start[s[a]].add(b)
        start[s[a]].remove(a)
        start[s[b]].remove(b)
        start[s[b]].add(a)
        s[a], s[b] = s[b], s[a]

        print(a+1, b+1)

