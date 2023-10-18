def helper(arr, curr, total, i):
    if i==0:
        return abs(total-2*curr)
    return min(helper(arr, curr+arr[i], total, i-1), helper(arr, curr, total, i-1))

n = int(input())
l = sorted(list(map(int, input().split())))
print(helper(l, 0, sum(l), n-1))