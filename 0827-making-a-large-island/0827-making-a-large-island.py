class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mp = {}
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        def check(r, c):
            nonlocal ans
            seen = set() 
            choice = 1
            for x, y in directions:  
                nr = r + x
                nc = c + y
                if 0 <= nr < rows and 0 <= nc < cols:
                    island_id = grid[nr][nc]
                    if island_id > 1 and island_id not in seen:  
                        seen.add(island_id) 
                        choice += mp[island_id]  
            ans = max(ans, choice)
            return ans
        visited = set()
        def dfs(r, c, id):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if (r, c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0
            size = 1
            visited.add((r, c))
            if grid[r][c] == 1:
                grid[r][c] = id
            for x, y in directions:
                nr = x + r
                nc = y + c
                size += dfs(nr, nc, id) 
            return size
        id = 2
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    val = dfs(i, j, id)
                    mp[id] = val 
                    id += 1
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    ans = max(ans,check(i, j))
        if ans == 0:
            return rows * cols
        return ans
            