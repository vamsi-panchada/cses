n = int(input())
l = list(map(int, input().split()))
ref = l[0]
i = 1
res = 1
print("starting")
while i<n:
    if l[i]<ref:
        ref = l[i]
        res += 1
    i+=1
print(res)