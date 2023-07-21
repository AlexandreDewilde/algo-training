def solve(n, l, start, end):
    current = [0] * n
    current[start] = 1
    for _ in range(l):
        new_l = current[:]        
        for i in range(n):
            if i > 0:
                new_l[i] += current[i - 1]
            if i + 1 < n:
                new_l[i] += current[i + 1]
            new_l[i] %= 5_318_008
        current = new_l
    return current[end]

for _ in range(int(input())):

    n = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    
    if abs(x1 - x2) > abs(y1 - y2):
        print(solve(n, abs(x1 - x2), y1 - 1, y2 - 1))
    else:
        print(solve(n, abs(y2 - y1), x1 - 1, x2 - 1))
