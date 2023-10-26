class QItem:
    def __init__(self, i, j, path, dist):
        self.i = i
        self.j = j
        self.path = path
        self.dist = dist

def isValid(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
        (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != '#') and (visited[x][y] == False)):
        return True
    return False

def getPath(A, grid):
    visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
    start = QItem(*A, '', 0)
    queue = []
    queue.append(start)
    visited[start.i][start.j] = True
    while queue:
        source = queue.pop(0)
        if grid[source.i][source.j]=='B':
            return source.path
        if isValid(source.i - 1, source.j, grid, visited):
            queue.append(QItem(source.i - 1, source.j, source.path+'U', source.dist + 1))
            visited[source.i - 1][source.j] = True
        if isValid(source.i + 1, source.j, grid, visited):
            queue.append(QItem(source.i + 1, source.j, source.path+'D', source.dist + 1))
            visited[source.i + 1][source.j] = True
        if isValid(source.i, source.j - 1, grid, visited):
            queue.append(QItem(source.i, source.j - 1, source.path+'L', source.dist + 1))
            visited[source.i][source.j - 1] = True
        if isValid(source.i, source.j + 1, grid, visited):
            queue.append(QItem(source.i, source.j + 1, source.path+'R', source.dist + 1))
            visited[source.i][source.j + 1] = True

def solve(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                return getPath((i, j), grid)

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