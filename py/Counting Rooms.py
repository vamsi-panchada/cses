def makeWall(i, j, n, m, grid, visited):
    queue = [(i, j)]
    while queue:
        (i, j) = queue.pop()
        visited[i][j]=True
        grid[i][j]='#'
        if i-1>=0 and not visited[i-1][j] and grid[i-1][j]=='.':
            queue.append((i-1, j))
        if i+1<n and not visited[i+1][j] and grid[i+1][j]=='.':
            queue.append((i+1, j))
        if j-1>=0 and not visited[i][j-1] and grid[i][j-1]=='.':
            queue.append((i, j-1))
        if j+1<m and not visited[i][j+1] and grid[i][j+1]=='.':
            queue.append((i, j+1))

def heler(grid):
    if len(grid)==0:
        return 0
    n=len(grid)
    m=len(grid[0])
    ans = 0
    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
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