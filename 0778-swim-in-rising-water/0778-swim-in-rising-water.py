from  heapq import heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxcost = [[float("inf")] * n for _ in range(n)]
        pq = []
        maxcost[0][0] = grid[0][0]
        heappush(pq, (grid[0][0],0,0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        while pq:
            currcost, r, c = heappop(pq)
            if currcost > maxcost[r][c]:
                continue
            for x, y in directions:
                nr = x + r
                nc = y + c
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                    newcost = max(currcost, grid[nr][nc])
                    if newcost < maxcost[nr][nc]:
                        maxcost[nr][nc] = newcost
                        heappush(pq, (newcost, nr, nc))
        return maxcost[rows-1][cols-1]
            