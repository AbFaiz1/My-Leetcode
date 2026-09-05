class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c, i):
            if r < 0  or c < 0 or r >= rows or c >= cols:
                return False
            if grid[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True 
            temp = grid[r][c]
            grid[r][c] = '#'
            for x, y in directions:
                nr = x + r
                nc = y + c
                if dfs(nr, nc, i+1):
                    return True
            grid[r][c] = temp
            return False
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False

