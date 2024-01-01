n, m, l = map(int, input().split())

F = list(map(int, input().split()))

C = list(map(int, input().split()))

intervals = []
prev = 0
head = l
coords = set(C)
coords.add(0)

for i, f in enumerate(F):
    if i % 2 == 0:
        intervals.append((prev, head - f))
        prev = head - f
        head = head - f - f
    else:
        intervals.append((prev, head + f))
        prev = head + f
        head = head + f + f
    coords.add(prev)

intervals.append((prev, head))
coords.add(head)

compressed = {c: i for i, c in enumerate(sorted(coords))}
compressed_inv = {i: c for c, i in compressed.items()}

import heapq

pq = []
intervals = ((min(x), max(x)) for x in intervals)
for it in intervals:
    heapq.heappush(pq, (it, 1))


current = 0
prev = 0
ans = []
for c in C + [int(1e25)]:
    nxt = current
    tot = 0
    while pq and pq[0][0][0] <= c:
        (start, end), move = heapq.heappop(pq)
        if move == 1:
            tot += min(end, c) - start
            if end > c:
                heapq.heappush(pq, ((end, -1), 0))
                nxt += 1
        else:
            tot += (start - prev)
            current -= 1
            nxt -= 1
    tot += (c - prev) * current
    ans.append(tot)
    current = nxt
    prev = c


print(" ".join(map(str, ans)))
