from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        queue.append((0, 0, 0, 0))

        visited = [[float('inf')] * cols for _ in range(rows)]
        visited[0][0] = 0

        while queue:
            row, col, dis, ok = queue.popleft()

            if row == rows - 1 and col == cols - 1:
                return dis

            for x, y in directions:
                nr = row + x
                nc = col + y

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_count = ok + grid[nr][nc]

                    if new_count <= k and new_count < visited[nr][nc]:
                        visited[nr][nc] = new_count
                        queue.append((nr, nc, dis + 1, new_count))

        return -1