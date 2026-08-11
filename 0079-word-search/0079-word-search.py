class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c, i):
            if r >= rows or c >= cols or r < 0 or c < 0:
                return 
            if i == len(word):
                return True
            if grid[r][c] != word[i] or grid[r][c] == "#":
                return                    
            temp = grid[r][c]
            grid[r][c] = "#"
            for x, y in directions:
                nr = x + r
                nc = y + c
                if dfs(nr, nc, i+1):
                    return True 
            grid[r][c] = temp          
            return 
        if len(grid) == 1 and len(grid[0]) == 1 and len(word) == 1:
            if grid[0][0] == word[0]:
                return True
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
    