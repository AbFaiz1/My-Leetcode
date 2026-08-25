import heapq
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        diff = [[float("inf")] * cols for _ in range(rows)]
        diff[0][0] = 0
        heap = []
        heapq.heappush(heap, (0, 0, 0))
        while heap:
            currdiff, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return currdiff
            if currdiff > diff[r][c]:
                continue
            for x, y in directions:
                nr = r + x
                nc = c + y
                if 0 <= nr < rows and 0 <= nc < cols:
                    edge_diff = abs(grid[nr][nc] - grid[r][c])
                    newdiff = max(currdiff, edge_diff)
                    if newdiff < diff[nr][nc]:
                        diff[nr][nc] = newdiff
                        heapq.heappush(
                            heap,
                            (newdiff, nr, nc)
                        )
        return 0