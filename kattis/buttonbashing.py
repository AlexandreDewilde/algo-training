from collections import deque
for _ in range(int(input())):
    n, t = map(int, input().split())
    
    poss = list(map(int, input().split()))
    
    dst = [float("inf")] * 3601

    queue = deque([0])
    dst[0] = 0
    while queue:
        x = queue.popleft()

        for time in poss:
            next_pos = min(max(0, x + time), 3600)
            if dst[next_pos] == float("inf"):
                dst[next_pos] = dst[x] + 1
                queue.append(next_pos)

    for i in range(t, 3601):
        if dst[i] != float("inf"):
            print(dst[i], i - t)
            break