r, c = map(int, input().split())

R = list(map(int, input().split()))
C = list(map(int, input().split()))

print("possible" if max(R) == max(C) else "impossible")