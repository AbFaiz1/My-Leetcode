class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if grid[r][c] == 1:
                return

            grid[r][c] = 1  
            for x, y in directions:
                dfs(r + x, c + y)

        for i in range(cols):
            if grid[0][i] == 0:
                dfs(0, i)  
            if grid[rows-1][i] == 0:
                dfs(rows-1, i) 

        for i in range(rows):
            if grid[i][0] == 0:
                dfs(i, 0) 
            if grid[i][cols-1] == 0:
                dfs(i, cols-1) 
        visited = set()
        def dfs2(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if (r, c) in visited or grid[r][c] == 1:
                return 
            visited.add((r, c))
            for x, y in directions:
                nr = x + r
                nc = y + c
                dfs2(nr, nc)
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i, j) not in visited:
                    dfs2(i, j)
                    ans += 1
        return ans
            