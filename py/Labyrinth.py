def path(i, j, n, m, grid, ans, dir):
    if i<0 or j<0 or i>=n or j>=m:
        return
    if grid[i][j]=='#':
        return
    else:
        
def solve(i, j, n, m, grid):
    ans = []
    if i-1>=0:
        p

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))
for i in range(n):
    for j in range(m):
        if grid[i][j]=='A':
            res = solve(i, j, n, m, grid)