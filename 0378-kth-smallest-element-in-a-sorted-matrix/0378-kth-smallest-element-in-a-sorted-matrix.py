class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def countLessEqual(mid):
            n = len(matrix)

            row = 0
            col = n - 1
            count = 0

            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    count += col + 1
                    row += 1
                else:
                    col -= 1

            return count

        n = len(matrix)

        low = matrix[0][0]
        high = matrix[n - 1][n - 1]

        while low < high:
            mid = (low + high) // 2

            count = countLessEqual(mid)

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low