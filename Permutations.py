n = int(input())
if n==1:
    print(1)
elif n<=3:
    print('NO SOLUTION')

else:
    se = ' '.join([str(i) for i in range(2, n+1, 2)])
    so = ' '.join([str(i) for i in range(1, n+1, 2)])
    print(se, so)