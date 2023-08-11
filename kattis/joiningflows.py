k = int(input())

l = [tuple(map(int, input().split())) for _ in range(k)]

base_temp = 0
base_flow = 0
for t, a, b in l:
    base_temp += t * a
    base_flow += a

l.sort()

def try_flow(target, minimize=True):
    if target < 0: return 0, -1
    temp = 0
    flow = target
    for t, a, b in (l if minimize else l[::-1]):
        temp += min(flow, b - a) * t
        flow -= min(flow, b - a)
    return temp, flow

for _ in range(int(input())):
    t, f = map(int, input().split())
    
    mintemp, rem = try_flow(f-base_flow)
    maxtemp, rem = try_flow(f-base_flow, False)
    print("yes" if rem == 0 and mintemp <= t*f - base_temp <= maxtemp else "no")
