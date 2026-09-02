from functools import lru_cache
class Solution:
    def largestSumOfAverages(self, arr: List[int], k: int) -> float:
        @lru_cache(None)
        def solve(i, group):
            if i == len(arr):
                return 0
            if group == k-1:
                return sum(arr[i:]) / (len(arr) - i)
            total = 0
            ans = 0
            for j in range(i, len(arr)):
                total += arr[j]
                c = (total / (j-i+1)) + solve(j+1, group+1)
                ans = max(ans, c)
            return ans
        return solve(0, 0)