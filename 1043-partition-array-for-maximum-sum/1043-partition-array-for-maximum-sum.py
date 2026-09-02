from functools import lru_cache
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def solve(i):
            if i == len(arr):
                return 0
            maxi = 0
            ans = 0
            for j in range(i, len(arr)):
                if j - i >= k:
                    break
                maxi = max(maxi, arr[j])
                c = maxi*(j-i+1) + solve(j+1)
                ans = max(ans, c)
            return ans
        return solve(0)