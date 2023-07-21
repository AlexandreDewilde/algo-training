for _ in range(int(input())):
    n = int(input())
    
    a = (list(map(int, input().split())))
    cnt = {}

    for el in a:
        cnt[el] = cnt.get(el, 0) + 1
    dp = [0] * (n + 1)
    
    for el, v in cnt.items():
        for i in range(el, n+1, el):
            dp[i] += v
            if dp[i] == n:
                print(n)
                break
        else:
            continue
        break
    else:
        print(max(dp))
        