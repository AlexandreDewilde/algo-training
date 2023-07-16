n = int(input())

ine = [int(input()) for _ in range(n)]

for a in range(10_002):
    for b in range(10_002):
        current = ine[0]
        ans = []
        for i in range(1, 2 * n):
            current = (a * current + b) % 10_001
            if i % 2:
                ans.append(current)
            elif current != ine[i // 2]:
                break
        else:
            print("\n".join(map(str, ans)))
            break
    else:
        continue
    break