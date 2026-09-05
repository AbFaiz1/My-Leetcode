from functools import lru_cache
class Solution:
    def rob(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        @lru_cache(None)
        def solve(i, j):
            if i > j:
                return 0
            if i == j:
                return arr[i]
            take = arr[i] + solve(i+2, j)
            skip = solve(i+1, j)
            return max(take, skip)
        ans = 0
        ans = max(solve(0,len(arr)-2), solve(1, len(arr)-1))
        return ans