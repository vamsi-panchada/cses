n, x = map(int, input().split())
l = list(map(int, input().split()))
d = {}
did = False
for i, j in enumerate(l):
    rem = x-j
    if j in d:
        print(d[j]+1, i+1)
        did=True
        break
    else:
        d[rem]=i
if not did:
    print('IMPOSSIBLE')