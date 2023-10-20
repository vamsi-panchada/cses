n = int(input())
l = sorted(list(map(int, input().split())))
res = 0
for i in l:
    if res+1<i:
        break
    res+=i
print(res+1)