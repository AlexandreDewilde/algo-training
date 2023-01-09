import sys

input = sys.stdin.readline

s = input()

n = int(input())

ss = 0
e = len(s)
for i in range(n):
    start, length = map(int, input().split())
    
    e = min(e,ss+start+length)
    ss += start

print(s[ss:e])
