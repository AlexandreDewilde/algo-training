import sys

sys.setrecursionlimit(int(1e6))
n = int(input())
mem = {0:0}
def dp(nb):
    if nb in mem:
        return mem[nb]
    d = nb % 10
    m = float("inf")
    if d <= 5:
        m = min(m, dp(nb//10)+d)
    if d >= 5:
        m = min(m, 10-d+dp(nb//10+1))

    mem[nb] = m
    return m
dp(n)
print(mem[n])