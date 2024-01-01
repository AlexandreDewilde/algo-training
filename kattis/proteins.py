n = int(input())
import sys

sys.setrecursionlimit(int(1e6))

s = input() + "__"

mem = {}
def dp(n, i):
    if (n, i) in mem:
        return mem[(n,i)]
    if n == 0:
        return 0

    if i >= len(s) - 2:
        return n * 3

    ret = float("inf")
    if s[i] == "A" and s[i+1] == "T" and s[i+2] == "G":
        return dp(n-1, i+3)
    if s[i:i+2] in {"AT", "AG", "TG"}:
        ret = min(ret, 1 + dp(n-1, i+2))
    if s[i] in "ATG":
        ret = min(ret, 2 + dp(n-1, i+1))
    ret = min(ret, dp(n, i+3))
    mem[(n, i)] = ret
    return ret

print(dp(n, 0))