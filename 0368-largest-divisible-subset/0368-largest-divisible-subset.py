from functools import lru_cache
class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        arr.sort()
        @lru_cache(None)
        def solve(i, last):
            if i == len(arr):
                return []
            skip = solve(i+1, last)
            take = []
            if last is None or arr[i] % last == 0:
                take = [arr[i]] + solve(i+1, arr[i])
            if len(take) > len(skip):
                return take
            return skip
        return solve(0, None)
