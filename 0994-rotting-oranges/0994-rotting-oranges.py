from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        dq = deque()

        rows = len(grid)
        cols = len(grid[0])

        fresh = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 2:
                    dq.append((i, j, 0))

                elif grid[i][j] == 1:
                    fresh += 1

        ans = 0

        while dq:

            r, c, mnt = dq.popleft()

            ans = max(ans, mnt)

            for x, y in directions:
                nr = r + x
                nc = c + y

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    dq.append((nr, nc, mnt + 1))

        if fresh > 0:
            return -1

        return ans