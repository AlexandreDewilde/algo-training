for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    best = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                continue
            best[i][j] = 1 + (best[i - 1][j] if i > 0 else 0)
    
    cnt = [0] * (n + m + 1)
    for i in range(n):
        stack = []
        for j in range(m):
            bestj = j
            while stack and stack[-1][1] > best[i][j]:
                if stack[-1][0] < bestj:
                    bestj = stack[-1][0]
                stack.pop()
            
            if grid[i][j] == "#":
                continue

            if not stack or j - stack[-1][0] + 1 + stack[-1][1] < j - bestj + 1 + best[i][j]:
                stack.append((bestj, best[i][j]))

            cnt[j - stack[-1][0] + 1 + stack[-1][1]] += 1
    
    for i in range(len(cnt)):
        if cnt[i] > 0:
            print(f"{cnt[i]} x {2 * i}")

