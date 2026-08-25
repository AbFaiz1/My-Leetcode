from typing import List
from bisect import bisect_left

class Solution:
    def mincostTickets(self, arr: List[int], costs: List[int]) -> int:
        n = len(arr)
        dp = [-1] * n
        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            i1 = bisect_left(arr, arr[i] + 1)
            i2 = bisect_left(arr, arr[i] + 7)
            i3 = bisect_left(arr, arr[i] + 30)
            dp[i] = min(
                costs[0] + solve(i1),
                costs[1] + solve(i2),
                costs[2] + solve(i3)
            )
            return dp[i]
        return solve(0)