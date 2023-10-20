n, m = map(int, input().split())
hn = sorted(list(map(int, input().split())), reverse=True)
tm = list(map(int, input().split()))
for i in tm:
    purchased = True
    for j in range(len(hn)):
        if i>=hn[j]:
            print(hn[j])
            hn.pop(j)
            purchased=False
            break
    if purchased:
        print(-1)