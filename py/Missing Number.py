n = int(input())
l = list(set(map(int, input().strip().split())))
c = None
for i in range(n-1):
    if i+1 != l[i]:
        c = i+1
        break
if not c:
    c = n
print(c)