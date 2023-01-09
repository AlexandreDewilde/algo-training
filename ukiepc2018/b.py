import sys

input = sys.stdin.readline


m, b, s = map(int, input().split())

ans = 0
for i in range(b):
    s = input()
    if s[m-1] == '1':
        ans |= int(s,2)

binary = bin(ans)
binary = binary[binary.index("b")+1:]
print(max(0,sum(map(int, str(binary)))-1))