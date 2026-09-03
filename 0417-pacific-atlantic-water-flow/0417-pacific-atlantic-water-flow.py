class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return
            ocean.add((r, c))
            for x, y in directions:
                nr = x + r
                nc = y + c
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                    if grid[nr][nc] >= grid[r][c]:
                        dfs(nr, nc, ocean)
        # pacific ocean
        for col in range(cols):
            dfs(0, col, pacific)
        for row in range(rows):
            dfs(row, 0, pacific)
        # atlantic ocean
        for row in range(rows):
            dfs(row, cols-1, atlantic)
        for col in range(cols):
            dfs(rows-1, col, atlantic)
        ans = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i,j) in atlantic:
                    ans.append([i, j])
        return ans