class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        total = 0
        mini = float("inf")
        for i in range(rows):
            for j in range(cols):
                if abs(matrix[i][j]) < mini:
                    mini = abs(matrix[i][j])
                total += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    count += 1
        if count % 2 == 0:
            return total
        return total - 2*mini
        
    