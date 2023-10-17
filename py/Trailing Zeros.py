n = int(input())
res = 0
mul = 5

while n/mul>=1:
    # print(res)
    res += n//mul
    mul*=5

print(res)