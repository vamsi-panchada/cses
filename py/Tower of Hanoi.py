l = []
def helper(n, s, d, a):
    if n==1:
        l.append((s, d))
        return 
    helper(n-1, s, a, d)
    l.append((s, d))
    helper(n-1, a, d, s)

n = int(input())
helper(n, 1, 3, 2)
print(len(l))
for i in l:
    print(*i)