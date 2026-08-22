class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]
        rows = len(matrix)
        cols = len(matrix[0])
        def check(mid):
            i = 0
            j = cols - 1
            count = 0
            while i < rows and j >= 0:
                if matrix[i][j] <= mid:
                    count += j + 1
                    i += 1
                else:
                    j -= 1
            return count
        while low <= high:
            mid = low + (high - low) // 2
            prevnum = check(mid)
            if prevnum < k:
                low = mid + 1
            else:
                high = mid - 1
        return low