class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mp = {}
        def solve(r, c):
            if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
                return float("inf")
            if r == len(matrix)-1:
                return matrix[r][c]
            if (r, c) in mp:
                return mp[(r, c)]
            choice1 = matrix[r][c] + solve(r+1, c-1)
            choice2 = matrix[r][c] + solve(r+1, c)
            choice3 = matrix[r][c] + solve(r+1, c+1)
            mp[(r, c)] =  min(choice1, choice2, choice3)
            return mp[(r, c)]
        ans = float("inf")
        for i in range(len(matrix)):
            ans = min(ans, solve(0, i))
        return ans
        