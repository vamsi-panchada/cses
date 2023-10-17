for _ in range(int(input())):
    l, r = map(int, input().split())
    if (l+r)%3 == 0 and min(l, r)*2 >= max(l, r):
        print('YES')
    else:
        print('NO')