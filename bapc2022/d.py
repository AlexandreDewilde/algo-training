n = int(input())

last = 0
ans = 0
for i in range(n):
    print(f"? {last} {i+1}")
    res = input()
    if res == "absent":
        ans += 1
        last = i+1
print(f"! {ans}")