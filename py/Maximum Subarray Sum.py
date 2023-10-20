n = int(input())
l = list(map(int, input().split()))
ans = sum(l)
locals = l[0]
for i in l[1:]:
    if locals<=0:
        locals=i
    else:
        locals+=i
    ans = max(locals, ans)
print(ans)