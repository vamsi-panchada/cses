def getPath(i, j, n, m, grid, visited, dir):
    if i<0 or i==n or j<0 or j==m or visited[i][j]:
        return 
    if grid[i][j]=='#':
        visited[i][j]=True
        return 
    if grid[i][j] == 'B':
        return dir
    if grid[i][j]!='#':
        visited[i][j]=True
        res = getPath(i-1, j, n, m, grid, visited, dir+'U')
        if res:
            return res
        res = getPath(i+1, j, n, m, grid, visited, dir+'D')
        if res:
            return res
        res = getPath(i, j-1, n, m, grid, visited, dir+'L')
        if res:
            return res
        res = getPath(i, j+1, n, m, grid, visited, dir+'R')
        if res:
            return res
        return


def solve(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                return getPath(i, j, n, m, grid, visited, '')

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))
res = solve(grid)
# print(res)
if res:
    print('YES')
    print(len(res))
    print(res)
else:
    print('NO')