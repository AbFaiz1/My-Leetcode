from bisect import bisect_right
from functools import lru_cache
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: (x[0], -x[1], x[0]))
        n = len(events)
        arr = [x[0] for x in events]
        @lru_cache(None)
        def solve(i, k):
            if i >= n:
                return 0
            if k <= 0:
                return 0
            skip = solve(i+1, k)
            idx = bisect_right(arr, events[i][1])
            take = events[i][2] + solve(idx, k-1)
            return max(skip, take)
        return solve(0, k)

        
