def solve(n, k):
    if n==1 or k==1:
        return 0
    i = '01'
    for _ in range(n-2):
        i = i + bin(int(i, 2)^2**(len(i)+1)-1)[3:]
        print(i)
    return int(i[k-1])
n, k = map(int, input().split())
print(solve(n, k))