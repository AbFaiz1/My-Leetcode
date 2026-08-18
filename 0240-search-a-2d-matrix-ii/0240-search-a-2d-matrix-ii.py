class Solution:
    def searchMatrix(self, grid: List[List[int]], target: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        r = 0
        c = cols-1
        while r < rows and c >= 0:
            if grid[r][c] == target:
                return True
            elif grid[r][c] > target:
                c -= 1
            else:
                r += 1
        return False