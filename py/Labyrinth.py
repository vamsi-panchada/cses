def path(grid, y, x):
    res = []
    while y!=0 and x!=0:
        if grid[y-1][x] == 'V':
            res.append('U')
        elif grid[y][x+1] == 'V':
            res.append('R')
        elif grid[y][x-1]=='V':
            res.append('L')
        elif grid[y+1][x] == 'V':
            res.append('D')
    return ''.join(res)


def solve(grid):
    queue = [(0, 0)]
    grid[0][0]='V'
    while queue:
        (y, x) = queue.pop(0)
        if grid[y][x] == 'B':
            return True, path(grid, y, x)
        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ny, nx = y+dy, x+dx
            grid[ny][nx] = 'V'
            if 0<=ny<len(grid) and 0<=nx<=len(grid[0]) and grid[ny][nx]!='#' and grid[ny][nx]!='V':
                queue.append((ny, nx))
    return False, None        



n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))
res, ans = solve(grid)
if res:
    print('YES')
    print(len(ans))
    print(ans)
else:
    print('NO')