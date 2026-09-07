from functools import lru_cache
class Solution:
    def largestSumOfAverages(self, arr: List[int], k: int) -> float:
        @lru_cache(None)
        def solve(i, groups):
            total = 0
            ans = 0
            if groups == k - 1:
                if i < len(arr):
                    return sum(arr[i:]) / (len(arr) - i)
                return float("-inf")
            for j in range(i, len(arr)):
                total += arr[j]
                c = (total / (j - i + 1)) + solve(j+1, groups + 1)
                ans = max(c, ans)
            return ans
        return solve(0, 0)

            
