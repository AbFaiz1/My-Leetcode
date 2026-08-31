from heapq import heappop, heappush

class Solution:

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        queries_sorted = sorted((val, i) for i, val in enumerate(queries))

        pq = []
        ans = [-1] * len(queries)

        j = 0

        for val, idx in queries_sorted:

            while j < len(intervals) and intervals[j][0] <= val:
                start, end = intervals[j]
                diff = end - start + 1

                heappush(pq, (diff, start, end))
                j += 1

            while pq and pq[0][2] < val:
                heappop(pq)

            if pq:
                ans[idx] = pq[0][0]

        return ans