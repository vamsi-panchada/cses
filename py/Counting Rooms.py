def makeWall(i, j, n, m, grid, visited): 
    if grid[i][j] == '#':
        visited[i][j]=True
        return
    else:
        grid[i][j]='#'
        visited[i][j]=True
        if i-1>=0 and not visited[i-1][j]:
            makeWall(i-1, j, n, m, grid, visited)
        if i+1<n and not visited[i+1][j]:
            makeWall(i+1, j, n, m, grid, visited)
        if j-1>=0 and not visited[i][j-1]:
            makeWall(i, j-1, n, m, grid, visited)
        if j+1<m and not visited[i][j+1]:
            makeWall(i, j+1, n, m, grid, visited)

def heler(grid):
    if len(grid)==0:
        return 0
    n=len(grid)
    m=len(grid[0])
    ans = 0
    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='.':
                ans += 1
                makeWall(i, j, n, m, grid, visited)
            else:
                visited[i][j]=True
    return ans

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(input()))
print(heler(l))