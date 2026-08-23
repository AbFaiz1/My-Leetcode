class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dq = deque()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if grid[r][c] == 'X' or grid[r][c] == '#':
                return 
            grid[r][c] = '#'
            for x, y in directions:
                nr = x + r
                nc = y + c
                dfs(nr, nc)
        for row in range(rows):
            if grid[row][0] == 'O':
                dfs(row, 0)
            if grid[row][cols-1] == 'O':
                dfs(row, cols-1)
        for col in range(cols):
            if grid[0][col] == 'O':
                dfs(0, col)
            if grid[rows-1][col] == 'O':
                dfs(rows-1, col)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '#':
                    grid[i][j] = 'O'
                elif grid[i][j] == 'O':
                    grid[i][j] = 'X'