n,k = map(int, input().split())

mem = {}
def dp(n, k, heads=0):
    if (n,k,heads) in mem:
        return mem[(n,k,heads)]
    if k == 0:
        return heads
    if n == heads:
        return dp(n,k-1, heads) + dp(n, k-1, heads-1)
    mem[(n,k,heads)] = dp(n,k-1, heads+1) + dp(n, k-1, heads)
    return mem[(n,k,heads)]

res = dp(n, k)
print(res/2**k)