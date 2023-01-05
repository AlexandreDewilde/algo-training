p,q = map(int, input().split())

if p & 1 and q & 1:
    print(1)
elif p & 1 and p < q:
    print(2)
else:
    print(0)