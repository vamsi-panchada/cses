n, m, k = map(int, input().split())
an = sorted(list(map(int, input().split())))
bm = sorted(list(map(int, input().split())))
ans = 0
i, j = 0, 0
while i<n and j<m:
    if an[i]-k<=bm[j]<=an[i]+k:
        i+=1
        j+=1
        ans+=1
    elif an[i]-k>bm[j]:
        j+=1
    elif an[i]+k<bm[j]:
        i+=1
print(ans)