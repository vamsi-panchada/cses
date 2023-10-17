n = int(input())
res = ['0', '1']
while n>1:
    temp = []
    for i in res:
        temp.append('0'+i)
    for i in res[::-1]:
        temp.append('1'+i)
    res = temp
    n-=1
print(*res, sep='\n')