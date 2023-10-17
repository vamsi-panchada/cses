n = int(input())
if n%4==0 or (n+1)%4==0:
    print('YES')
    if n%2==0:
        print(n//2)
        for i in range(1, n, 2):
            print(i, end=' ')
        print(n//2)
        for i in range(2, n, 2):
            print(i, end=' ')
    else:
        if n%8==0:
            print(n//2+1)
            for i in range(1, n, 2):
                print(i, end=' ')
            print(n)
            print(n//2)
            for i in range(2, n, 2):
                print(i, end=' ')
        else:
            print(n//2)
            for i in range(1, n, 2):
                print(i, end=' ')
            print()
            print(n//2+1)
            for i in range(2, n, 2):
                print(i, end=' ')
            print(n)
else:
    print('NO')