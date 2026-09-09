from functools import lru_cache
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        @lru_cache(None)
        def solve(i):
            if i == len(arr):
                return 0
            ans = 1
            for j in range(i+1, len(arr)):
                if arr[j] <= arr[i]:
                    continue
                c = solve(j)
                ans = max(ans,1+c)
            return ans
        ans = 0 
        for i in range(len(arr)): 
            ans = max(ans,solve(i))
        return ans