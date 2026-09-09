from functools import lru_cache
class Solution:
    def canJump(self, arr: List[int]) -> bool:
        @lru_cache(None)
        def solve(i):
            if i == len(arr) - 1:
                return True
            if arr[i] == 0:
                return False
            for newIndex in range(i+1, i+arr[i]+1):
                if solve(newIndex):
                    return True
            return False
        return solve(0)
        