n, m, k = map(int, input().split())

a = [int(input()) for _ in range(n)] + [0] * m
ans = 0

flights = 0
paid = [0] * len(a)
current_paid = 0

for i in range(len(a)):
    flights += a[i]
    if i - m >= 0:
        flights -= a[i-m]
        current_paid -= paid[i-m]
    j = i
    while j >= 0 and j > i - m and k - current_paid > 0 and flights - current_paid > 0:
        payed = min(k - current_paid, a[j] - paid[j])
        paid[j] += payed
        current_paid += payed
        ans += payed
        j -= 1

print(ans)