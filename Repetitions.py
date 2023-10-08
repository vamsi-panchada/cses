s = input()
res = 0
counter=1
validator = s[0]
for i in s[1:]:
    if i==validator:
        counter+=1
    else:
        validator=i
        res = max(res, counter)
        counter=1
print(max(res, counter))