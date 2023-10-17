from collections import defaultdict
s = input()
d = defaultdict(int)
for i in s:
    # print(i)
    d[i]+=1
odd = 0
oddchar = ''
oddcharcount=0
for i,j in d.items():
    if j%2!=0:
        odd += 1
        oddchar = i
        oddcharcount = j


if odd>1 or odd==1 and len(s)%2 == 0:
    print('NO SOLUTION')
else:
    lh, rh = '', ''
    # print(d)
    for i, j in d.items():
        if j%2 == 0:
            t = i*(j//2)
            lh = lh+t
            rh = t+rh
    print(lh+oddchar*oddcharcount+rh)