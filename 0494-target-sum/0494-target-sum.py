class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        map = {}
        def solve(i, val):
            if i == len(arr):
                if val == target:
                    return 1
                return 0
            if i >= len(arr):
                return 0
            if (i, val) in map:
                return map[(i, val)]
                return dp[i][val]
            option1 = solve(i+1, val+arr[i])
            option2 = solve(i+1, val-arr[i])
            map[(i, val)] = option1 + option2
            return map[(i, val)]
        return solve(0, 0)
            