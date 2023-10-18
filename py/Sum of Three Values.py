def helper(l, x):
    l = [(i, j) for i, j in enumerate(l)]
    l.sort(key = lambda x: x[-1])
    for i in range(0, len(l)-2):
        lp = i+1
        rp = len(l)-1
        while lp<rp:
            if l[i][1]+l[lp][1]+l[rp][1]==x:
                return [l[i][0]+1, l[lp][0]+1, l[rp][0]+1]
            elif l[i][1]+l[lp][1]+l[rp][1] < x:
                lp+=1
            else:
                rp-=1
    return None

n, x = map(int, input().split())
l = list(map(int, input().split()))

res = helper(l, x)

if res:
    print(*res)
else:
    print('IMPOSSIBLE')