n, x = map(int, input().split())
l = sorted(list(map(int, input().split())))
lp, rp = 0, n-1
c=0
while lp<rp:
    if l[lp]+l[rp]<=x:
        lp+=1
        rp-=1
    else:
        rp-=1
    c+=1
if lp==rp:
    c+=1
print(c)