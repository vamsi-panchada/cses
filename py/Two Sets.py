n = int(input())
s = (n+1)*n//2
if s%2==0:
    print('YES')
    t = s//2
    l, r = [], []
    for i in range(n, 0, -1):
        if i<=t:
            l.append(i)
            t-=i
        else:
            r.append(i)
    print(len(l))
    print(*l)
    print(len(r))
    print(*r)
    
else:
    print('NO')