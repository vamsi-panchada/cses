n = int(input())
l = list(map(int, input().split()))
res = 0
i = 1
while i<n:
    if l[i-1]>l[i]:
        res += (l[i-1]-l[i])
        l[i]=l[i-1]
    i+=1
print(res)