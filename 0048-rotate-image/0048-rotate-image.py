class Solution:
    def rotate(self, grid: List[List[int]]) -> None:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited:
                    continue
                visited.add((i,j))
                visited.add((j,i))
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
        visited.clear()
        for i in range(rows):
            for j in range(cols):
                if (i, j) in visited:
                    continue
                visited.add((i,j))
                visited.add((i,cols-j-1))
                grid[i][j], grid[i][cols-j-1] = grid[i][cols-j-1], grid[i][j]
        
                

        