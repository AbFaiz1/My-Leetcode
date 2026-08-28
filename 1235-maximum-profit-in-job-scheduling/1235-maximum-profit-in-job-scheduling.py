from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = list(zip(startTime, endTime, profit))
        arr.sort()
        mp = {}
        starts = [x[0] for x in arr]
        def solve(i):
            if i >= len(arr):
                return 0
            if i in mp:
                return mp[i]
            skip = solve(i + 1)
            j = bisect_left(starts, arr[i][1])
            take = arr[i][2] + solve(j)
            mp[i] = max(take, skip)
            return mp[i]
        return solve(0)