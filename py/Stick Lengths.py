n = int(input())
l = sorted(list(map(int, input().split())))
med = l[n//2]
cost = 0
for i in l:
    cost += abs(i-med)
print(cost)