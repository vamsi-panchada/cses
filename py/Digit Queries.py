for _ in range(int(input())):
    k=int(input())
    i = 1
    while k>(9*i*(10**(i-1))):
        k-=(9*i*(10**(i-1)))
        i+=1
    rem = k//i
    mod = k%i
    num = 10**(i-1)+rem-1
    print(str(num)[mod-1])
    