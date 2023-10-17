for _ in range(int(input())):
    x, y = map(int, input().split())
    maxx = max(x, y)
    t = (maxx-1)**2
    if t%2 == 0:
        t = t+maxx+y-x
    else:
        t = t+maxx-y+x
    print(t)
