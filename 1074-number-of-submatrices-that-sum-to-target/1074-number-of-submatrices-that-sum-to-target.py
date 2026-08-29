class Solution:

    def numSubmatrixSumTarget(self, grid: List[List[int]], target: int) -> int:

        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        for top in range(rows):

            col = [0] * cols

            for bottom in range(top, rows):

                for c in range(cols):
                    col[c] += grid[bottom][c]

                freq = {0: 1}
                prefix = 0

                for c in range(cols):
                    prefix += col[c]

                    ans += freq.get(prefix - target, 0)

                    freq[prefix] = freq.get(prefix, 0) + 1

        return ans